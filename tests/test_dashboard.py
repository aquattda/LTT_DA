"""Run with: python -m unittest discover -s tests -v.

Uses real CSVs and Streamlit AppTest. Prediction UI tests replace only the
expensive estimator boundary; they do not claim to validate model accuracy.
"""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Do_An/walmart_eda_model"))
import streamlit_dashboard as dashboard


class ScenarioModel:
    feature_names = dashboard.MODEL_FEATURES
    feature_importances_ = np.full(12, 1 / 12)
    validation_r2 = .75

    class Encoder:
        @staticmethod
        def transform(values):
            return [{"A": 0, "B": 1, "C": 2}[value] for value in values]

    label_encoder = Encoder()

    def predict(self, frame):
        self.frame = frame.copy()
        return np.array([12345.0])


class DashboardTest(unittest.TestCase):
    def app(self):
        app = AppTest.from_string(
            "import streamlit_dashboard as dashboard\ndashboard.main()",
            default_timeout=60,
        ).run()
        self.assertFalse(app.exception, [x.message for x in app.exception])
        return app

    def assert_clean(self, app):
        self.assertFalse(app.exception, [x.message for x in app.exception])

    def test_all_pages_render_without_training(self):
        data, _ = dashboard.load_data()
        original_columns = data.columns.tolist()
        with patch.object(dashboard, "train_model", side_effect=AssertionError("Training must be opt-in")) as train:
            app = self.app()
            for name in dashboard.PAGES:
                with self.subTest(page=name):
                    app.radio(key="page").set_value(name).run()
                    self.assert_clean(app)
                    if name != "Dự đoán doanh số":
                        self.assertGreater(len(app.get("plotly_chart")), 0)
            train.assert_not_called()
        self.assertEqual(data.columns.tolist(), original_columns)

    def test_filters_empty_reset_and_partial_holiday_year(self):
        app = self.app()
        app.multiselect(key="filter_types").set_value([]).run()
        self.assert_clean(app)
        self.assertEqual(len(app.get("plotly_chart")), 0)
        self.assertGreater(len(app.info), 0)
        reset = next(b for b in app.button if b.label == "Đặt lại bộ lọc")
        reset.click().run()
        self.assert_clean(app)
        self.assertEqual(app.multiselect(key="filter_types").value, ["A", "B", "C"])
        app.multiselect(key="filter_types").set_value(["C"]).run()
        app.multiselect(key="filter_years").set_value([2012]).run()
        summary = app.dataframe[0].value
        self.assertEqual(summary.Type.tolist(), ["C"])
        data, _ = dashboard.load_data()
        subset = data[(data.Type == "C") & (data.Year == 2012)]
        self.assertEqual(summary.Stores.iloc[0], subset.Store.nunique())
        self.assertAlmostEqual(summary.Sales.iloc[0], subset.Weekly_Sales.sum())
        app.radio(key="page").set_value("Ngày lễ & mùa vụ").run()
        self.assert_clean(app)
        self.assertTrue(any("45–52" in message.value for message in app.info))
        app.multiselect(key="filter_years").set_value([]).run()
        self.assert_clean(app)
        self.assertEqual(len(app.get("plotly_chart")), 0)

    def test_time_granularity_and_store_totals(self):
        app = self.app()
        app.radio(key="page").set_value("Xu hướng thời gian").run()
        app.radio(key="time_resolution").set_value("Theo tháng").run()
        self.assert_clean(app)
        app.radio(key="page").set_value("Hiệu suất cửa hàng").run()
        self.assert_clean(app)
        performance = app.dataframe[0].value.set_index("Store")
        data, _ = dashboard.load_data()
        reference = data.groupby(["Store", "Date"]).Weekly_Sales.sum().groupby("Store").mean()
        np.testing.assert_allclose(performance.loc[reference.index, "Avg_Weekly"], reference)
        np.testing.assert_allclose(performance.Sales_per_sqft, performance.Avg_Weekly / performance.Size * 1000)
        app.selectbox(key="detail_store").select_index(1).run()
        self.assert_clean(app)

    def test_prediction_form_result_and_snapshot(self):
        model = ScenarioModel()
        with patch.object(dashboard, "train_model", return_value=model) as train:
            app = self.app()
            app.radio(key="page").set_value("Dự đoán doanh số").run()
            train.assert_not_called()
            app.slider(key="prediction_week").set_value(12)
            app.checkbox(key="prediction_holiday").check()
            submit = next(b for b in app.button if "Tạo dự đoán" in b.label)
            submit.click().run()
            self.assert_clean(app)
            train.assert_called_once()
            result = app.session_state["prediction_result"]
            self.assertEqual(result["prediction"], 12345.0)
            self.assertEqual(result["week"], 12)
            self.assertTrue(result["holiday"])
            self.assertEqual(list(model.frame.columns), dashboard.MODEL_FEATURES)
            self.assertEqual(model.frame.IsHoliday_encoded.iloc[0], 1)
            self.assertEqual(model.frame.Month.iloc[0], 3)
            self.assertGreater(len(app.get("plotly_chart")), 0)
            # A changed store must not relabel the previous result as a new prediction.
            previous_store = result["store"]
            app.selectbox(key="prediction_store").select_index(1).run()
            self.assert_clean(app)
            self.assertEqual(app.session_state["prediction_result"]["store"], previous_store)
            train.assert_called_once()

    def test_training_dependency_error_is_visible(self):
        with patch.object(dashboard, "train_model", side_effect=ImportError("Unavailable estimator")):
            app = self.app()
            app.radio(key="page").set_value("Dự đoán doanh số").run()
            next(b for b in app.button if "Tạo dự đoán" in b.label).click().run()
            self.assert_clean(app)
            self.assertTrue(any("scikit-learn" in error.value for error in app.error))

    def test_windows_policy_error_has_actionable_message(self):
        with patch.object(dashboard, "train_model", side_effect=ImportError(
            "DLL load failed: An Application Control policy has blocked this file."
        )):
            app = self.app()
            app.radio(key="page").set_value("Dự đoán doanh số").run()
            next(b for b in app.button if "Tạo dự đoán" in b.label).click().run()
            self.assert_clean(app)
            self.assertTrue(any("Windows" in error.value for error in app.error))
            self.assertTrue(any("python run_project.py doctor" in code.value for code in app.code))
            self.assertNotIn("prediction_result", app.session_state)


if __name__ == "__main__":
    unittest.main()
