"""Regression coverage for main filters, branding and navigation events."""
from pathlib import Path
from base64 import b64decode
import sys
import unittest

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'Do_An/walmart_eda_model'))
import streamlit_dashboard as dashboard
from dashboard_ui import logo_data_uri


class FilterNavigationTest(unittest.TestCase):
    def app(self):
        app = AppTest.from_string('import streamlit_dashboard as dashboard\ndashboard.main()', default_timeout=60).run()
        self.clean(app)
        return app

    def clean(self, app):
        self.assertFalse(app.exception, [error.message for error in app.exception])

    def test_filter_location_and_original_logo(self):
        app = self.app()
        self.assertEqual(len(app.sidebar.multiselect), 0)
        self.assertEqual(len(app.date_input), 0)
        self.assertEqual(len(app.main.multiselect), 2)
        self.assertTrue(any('alt="Walmart"' in m.value for m in app.sidebar.markdown))
        source = ROOT / 'Do_An/walmart_eda_model/Walmart-Logo-New.png'
        self.assertEqual(b64decode(logo_data_uri().split(',', 1)[1]), source.read_bytes())

    def test_combined_month_year_type_filters_and_reset(self):
        app = self.app()
        app.multiselect(key='filter_types').set_value(['A']).run()
        app.multiselect(key='filter_years').set_value([2011]).run()
        app.selectbox(key='filter_month').set_value(11).run()
        self.clean(app)
        data, _ = dashboard.load_data()
        reference = data[(data.Type == 'A') & (data.Year == 2011) & (data.Month == 11)]
        self.assertAlmostEqual(app.dataframe[0].value.Sales.sum(), reference.Weekly_Sales.sum(), delta=.01)
        self.assertFalse(any('navigation-scroll-marker' in e.proto.body for e in app.get('html')))
        next(b for b in app.button if b.label == 'Đặt lại bộ lọc').click().run()
        self.clean(app)
        self.assertEqual(app.selectbox(key='filter_month').value, 0)
        self.assertAlmostEqual(app.dataframe[0].value.Sales.sum(), data.Weekly_Sales.sum(), delta=.01)

    def test_empty_month_scope(self):
        app = self.app()
        app.multiselect(key='filter_years').set_value([2012]).run()
        app.selectbox(key='filter_month').set_value(12).run()
        self.clean(app)
        self.assertEqual(len(app.get('plotly_chart')), 0)
        self.assertTrue(any('Không có dữ liệu' in info.value for info in app.info))

    def test_navigation_scroll_event_and_filter_persistence(self):
        app = self.app()
        revision = app.session_state['_navigation_revision']
        app.selectbox(key='filter_month').set_value(11).run()
        app.multiselect(key='filter_years').set_value([2011]).run()
        self.assertEqual(app.session_state['_navigation_revision'], revision)
        app.radio(key='page').set_value('Khám phá dữ liệu').run()
        self.clean(app)
        self.assertEqual(app.session_state['_navigation_revision'], revision + 1)
        app.radio(key='page').set_value('Dự đoán doanh số').run()
        self.clean(app)
        app.run()
        app.radio(key='page').set_value('Tổng quan').run()
        self.clean(app)
        self.assertEqual(app.session_state['_navigation_revision'], revision + 3)
        self.assertEqual(app.selectbox(key='filter_month').value, 11)
        self.assertEqual(app.multiselect(key='filter_years').value, [2011])
        scripts = [element.proto for element in app.get('html') if 'navigation-scroll-marker' in element.proto.body]
        self.assertEqual(len(scripts), 1)
        self.assertTrue(scripts[0].unsafe_allow_javascript)
        app.run()
        self.assertEqual(app.session_state['_navigation_revision'], revision + 3)
        self.assertFalse(any('navigation-scroll-marker' in e.proto.body for e in app.get('html')))


if __name__ == '__main__':
    unittest.main()
