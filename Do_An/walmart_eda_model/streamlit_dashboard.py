"""Walmart Sales Intelligence — interactive historical sales workspace."""
from pathlib import Path
import logging

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from dashboard_ui import (
    COLORS, GOLD, LABELS, NAVY, TEAL, TYPE_COLORS,
    chart, empty_state, insight, metrics, money, page_header, panel, setup_ui,
    brand_logo, scroll_to_top_on_navigation,
)

PAGES = {
    "Tổng quan": ("01   Tổng quan", "Bức tranh kinh doanh", "Theo dõi doanh số, xu hướng và hiệu suất của toàn hệ thống."),
    "Khám phá dữ liệu": ("02   Khám phá dữ liệu", "Khám phá dữ liệu", "Nhìn sâu vào phân phối doanh số và đặc điểm cửa hàng."),
    "Xu hướng thời gian": ("03   Xu hướng thời gian", "Nhịp điệu doanh số", "Khám phá xu hướng theo tuần, tháng và mùa trong năm."),
    "Yếu tố tác động": ("04   Yếu tố tác động", "Các yếu tố tác động", "Khảo sát mối liên hệ giữa doanh số và các chỉ số kinh tế."),
    "Ngày lễ & mùa vụ": ("05   Ngày lễ & mùa vụ", "Ngày lễ & mùa vụ", "So sánh tuần lễ với tuần thường và nhận diện mùa cao điểm."),
    "Dự đoán doanh số": ("06   Dự đoán doanh số", "Từ dữ liệu đến dự đoán", "Thiết lập một kịch bản để ước tính doanh số cửa hàng và bộ phận."),
    "Hiệu suất cửa hàng": ("07   Hiệu suất cửa hàng", "Hiệu suất cửa hàng", "So sánh các cửa hàng và khám phá bộ phận dẫn đầu."),
}
MODEL_FEATURES = [
    "Store", "Dept", "Size", "Type_encoded", "Temperature", "Fuel_Price",
    "CPI", "Unemployment", "IsHoliday_encoded", "Year", "Month", "Week",
]


@st.cache_data(show_spinner=False)
def load_data():
    dataset_dir = Path(__file__).resolve().parent.parent / "dataset"
    stores = pd.read_csv(dataset_dir / "stores.csv")
    features = pd.read_csv(dataset_dir / "features.csv")
    frames = []
    for filename in ("train.csv", "test.csv"):
        df = pd.read_csv(dataset_dir / filename)
        df = df.merge(stores, on="Store", how="left")
        df = df.merge(features, on=["Store", "Date", "IsHoliday"], how="left")
        df["Date"] = pd.to_datetime(df["Date"])
        for name, values in {
            "Year": df.Date.dt.year, "Month": df.Date.dt.month,
            "Week": df.Date.dt.isocalendar().week.astype(int), "Quarter": df.Date.dt.quarter,
        }.items():
            df[name] = values
        markdown = [f"MarkDown{i}" for i in range(1, 6)]
        df[markdown] = df[markdown].fillna(0)
        if filename == "test.csv":
            df[["CPI", "Unemployment"]] = df[["CPI", "Unemployment"]].fillna(0)
        frames.append(df)
    return tuple(frames)


@st.cache_resource(show_spinner=False)
def train_model(walmart_data):
    """Fit the existing Gradient Boosting configuration on the full training scope."""
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder

    df = walmart_data.copy()
    encoder = LabelEncoder()
    df["Type_encoded"] = encoder.fit_transform(df["Type"])
    df["IsHoliday_encoded"] = df["IsHoliday"].astype(int)
    X = df[MODEL_FEATURES].dropna()
    y = df.loc[X.index, "Weekly_Sales"]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor(n_estimators=100, max_depth=15, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)
    model.label_encoder = encoder
    model.feature_names = MODEL_FEATURES
    model.validation_r2 = model.score(X_val, y_val)
    model.training_r2 = model.score(X_train, y_train)
    return model


def reset_filters():
    st.session_state["filter_types"] = st.session_state["available_types"]
    st.session_state["filter_years"] = st.session_state["available_years"]
    st.session_state["filter_month"] = 0


def sidebar():
    with st.sidebar:
        brand_logo()
        st.markdown('<div class="sidebar-label">KHÔNG GIAN PHÂN TÍCH</div>', unsafe_allow_html=True)
        page = st.radio("Điều hướng", list(PAGES), format_func=lambda x: PAGES[x][0], key="page", label_visibility="collapsed")
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-foot"><b>Walmart Weekly Sales</b><br>Phân tích dữ liệu lịch sử<br>Đơn vị tiền tệ · USD</div>', unsafe_allow_html=True)
    return page


def filter_bar(data):
    """Shared type/year/month filters in the main content area."""
    types = sorted(data.Type.unique())
    years = sorted(int(x) for x in data.Year.unique())
    st.session_state.update(available_types=types, available_years=years)
    defaults = {"filter_types": types, "filter_years": years,
                "filter_month": 0}
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)
    with st.container(border=True, key="main_filters"):
        st.markdown('<h3 class="panel-title">Phạm vi phân tích</h3>', unsafe_allow_html=True)
        type_col, year_col, month_col = st.columns([1.2, 1.4, 1])
        with type_col:
            selected_types = st.multiselect("Loại cửa hàng", types, key="filter_types")
        with year_col:
            selected_years = st.multiselect("Năm phân tích", years, key="filter_years")
        with month_col:
            selected_month = st.selectbox("Tháng", range(13), key="filter_month",
                                          format_func=lambda x: "Tất cả các tháng" if x == 0 else f"Tháng {x:02d}")
        selected = data[data.Type.isin(selected_types) & data.Year.isin(selected_years)]
        if selected_month:
            selected = selected[selected.Month == selected_month]
        summary_col, reset_col = st.columns([4, 1])
        with summary_col:
            st.caption(f"{len(selected):,} / {len(data):,} bản ghi · Các bộ lọc được áp dụng đồng thời.")
        with reset_col:
            st.button("Đặt lại bộ lọc", on_click=reset_filters, width="stretch")
    return selected


def weekly_series(data):
    return data.groupby("Date", as_index=False).Weekly_Sales.sum().sort_values("Date")


def sales_line(data, height=310):
    fig = px.area(data, x="Date", y="Weekly_Sales", color_discrete_sequence=[TEAL])
    fig.update_traces(line_width=2.5, fillcolor="rgba(15,136,123,.08)", hovertemplate="%{x|%d/%m/%Y}<br><b>$%{y:,.0f}</b><extra></extra>")
    fig.update_layout(hovermode="x unified")
    fig.update_xaxes(title=None)
    fig.update_yaxes(title="Doanh số (USD)", tickprefix="$", tickformat="~s")
    chart(fig, height)


def ranked_bar(values, prefix, color=TEAL, height=310):
    values = values.sort_values()
    labels = [f"{prefix} {x}" for x in values.index]
    fig = go.Figure(go.Bar(x=values.values, y=labels, orientation="h", marker_color=color,
                          hovertemplate="%{y}<br>$%{x:,.0f}<extra></extra>"))
    fig.update_xaxes(tickprefix="$", tickformat="~s")
    chart(fig, height, horizontal=True)


def distribution_box(data, group):
    """Render full-data quartiles without sending hundreds of thousands of points."""
    fig = go.Figure()
    for i, (name, part) in enumerate(data.groupby(group, observed=True)):
        values = part.Weekly_Sales.dropna()
        q1, median, q3 = values.quantile([.25, .5, .75])
        iqr = q3 - q1
        lower = values[values >= q1 - 1.5 * iqr].min()
        upper = values[values <= q3 + 1.5 * iqr].max()
        fig.add_trace(go.Box(name=str(name), q1=[q1], median=[median], q3=[q3],
                            lowerfence=[lower], upperfence=[upper], boxpoints=False,
                            marker_color=TYPE_COLORS.get(name, COLORS[i % len(COLORS)])))
    fig.update_layout(showlegend=False)
    fig.update_yaxes(title="Doanh số / bộ phận / tuần (USD)", tickprefix="$", tickformat="~s")
    return fig


def overview_page(data):
    weekly = weekly_series(data)
    metrics([
        ("Tổng doanh số", money(data.Weekly_Sales.sum(), True), "Tổng trong phạm vi đang chọn"),
        ("Doanh số / tuần", money(weekly.Weekly_Sales.mean(), True), "Trung bình toàn hệ thống / tuần có dữ liệu"),
        ("Cửa hàng", data.Store.nunique(), "Số cửa hàng trong phạm vi"),
        ("Bộ phận", data.Dept.nunique(), f"{len(data):,} bản ghi doanh số"),
    ])
    left, right = st.columns([1.9, 1])
    with left, panel("Diễn biến doanh số", "Tổng doanh số toàn hệ thống theo từng tuần có dữ liệu"):
        sales_line(weekly)
    with right, panel("Cơ cấu doanh số", "Tỷ trọng doanh số theo loại cửa hàng"):
        totals = data.groupby("Type").Weekly_Sales.sum()
        fig = go.Figure(go.Pie(labels=totals.index, values=totals.values, hole=.76,
                              marker_colors=[TYPE_COLORS[x] for x in totals.index], sort=False,
                              textinfo="percent", textposition="outside", textfont_size=11,
                              hovertemplate="Loại %{label}<br>$%{value:,.0f}<br>%{percent}<extra></extra>"))
        fig.add_annotation(text=f"<b>{data.Store.nunique()}</b><br>cửa hàng", x=.5, y=.5, showarrow=False, font_size=19, font_color=NAVY)
        fig.update_layout(legend=dict(x=.12))
        chart(fig, 310)
    left, right = st.columns([1.25, 1])
    with left, panel("10 bộ phận dẫn đầu", "Xếp hạng theo doanh số trung bình / cửa hàng / tuần"):
        top = data.groupby("Dept").Weekly_Sales.mean().nlargest(10)
        ranked_bar(top, "Bộ phận", height=330)
    with right, panel("Đặc điểm mạng lưới", "Số cửa hàng duy nhất và doanh số theo loại"):
        summary = data.groupby("Type").agg(Stores=("Store", "nunique"), Sales=("Weekly_Sales", "sum"), Average=("Weekly_Sales", "mean")).reset_index()
        st.dataframe(summary, hide_index=True, width="stretch", column_config={
            "Type": "Loại", "Stores": "Cửa hàng",
            "Sales": st.column_config.NumberColumn("Tổng doanh số ($)", format="$%.0f"),
            "Average": st.column_config.NumberColumn("TB / bộ phận / tuần ($)", format="$%.0f"),
        })
        best = summary.loc[summary.Average.idxmax()]
        insight(f"Loại {best.Type} dẫn đầu về doanh số trung bình", f"{money(best.Average)} / bộ phận / tuần; gồm {int(best.Stores)} cửa hàng trong phạm vi đang chọn.")
        st.caption("Các số trung bình theo bộ phận khác với tổng doanh số toàn cửa hàng.")


def eda_page(data):
    metrics([
        ("Số quan sát", f"{len(data):,}", "Mỗi dòng là một cửa hàng · bộ phận · tuần"),
        ("Trung vị doanh số", money(data.Weekly_Sales.median()), "Theo bộ phận / tuần"),
        ("Độ lệch chuẩn", money(data.Weekly_Sales.std()), "Mức phân tán doanh số theo bản ghi"),
    ])
    left, right = st.columns(2)
    with left, panel("Diện tích & doanh số", "Mỗi điểm đại diện cho một cửa hàng"):
        stores = data.groupby("Store").agg(Size=("Size", "first"), Weekly_Sales=("Weekly_Sales", "mean"), Type=("Type", "first")).reset_index()
        fig = px.scatter(stores, x="Size", y="Weekly_Sales", color="Type", hover_name="Store", color_discrete_map=TYPE_COLORS)
        fig.update_traces(marker_size=12, marker_opacity=.8, marker_line_width=1, marker_line_color="white")
        fig.update_yaxes(title="TB / bộ phận / tuần (USD)")
        chart(fig)
    with right, panel("Phân phối doanh số", "Toàn bộ bản ghi · 50 khoảng doanh số"):
        counts, edges = np.histogram(data.Weekly_Sales, bins=50)
        fig = go.Figure(go.Bar(x=(edges[:-1] + edges[1:]) / 2, y=counts, width=np.diff(edges) * .93, marker_color=TEAL))
        fig.add_vline(x=data.Weekly_Sales.mean(), line_dash="dot", line_color=GOLD)
        fig.update_xaxes(title="Doanh số / bộ phận / tuần (USD)", tickformat="~s")
        fig.update_yaxes(title="Số bản ghi")
        chart(fig)
        st.caption("Đường vàng: doanh số trung bình. Bao gồm cả giá trị âm nếu có.")
    left, right = st.columns(2)
    with left, panel("Phân phối theo loại cửa hàng", "Trung vị, tứ phân vị và râu 1,5 × IQR; không vẽ điểm ngoại lệ"):
        chart(distribution_box(data, "Type"), 350)
    with right, panel("Ma trận tương quan", "Hệ số Pearson · từ −1 đến +1"):
        cols = ["Weekly_Sales", "Size", "Temperature", "Fuel_Price", "CPI", "Unemployment"]
        corr = data[cols].corr().rename(index=LABELS, columns=LABELS)
        fig = px.imshow(corr, text_auto=".2f", aspect="auto", zmin=-1, zmax=1,
                        color_continuous_scale=[NAVY, "#F7F9FC", TEAL])
        fig.update_layout(coloraxis_showscale=False)
        chart(fig, 350)


def time_analysis_page(data):
    weekly = weekly_series(data)
    peak = weekly.loc[weekly.Weekly_Sales.idxmax()]
    metrics([
        ("Tuần cao nhất", money(peak.Weekly_Sales, True), f"Tuần kết thúc {peak.Date:%d/%m/%Y}"),
        ("Số tuần quan sát", len(weekly), "Chỉ tính tuần có dữ liệu"),
        ("TB / bộ phận / tuần", money(data.Weekly_Sales.mean()), "Trong phạm vi đang chọn"),
    ])
    with panel("Doanh số theo thời gian", "Tổng doanh số; tháng đầu/cuối hoặc năm chưa đủ có thể không so sánh trực tiếp"):
        resolution = st.radio("Độ chi tiết", ["Theo tuần", "Theo tháng"], horizontal=True, key="time_resolution")
        series = weekly if resolution == "Theo tuần" else data.groupby(data.Date.dt.to_period("M")).Weekly_Sales.sum().rename_axis("Date").reset_index()
        if resolution == "Theo tháng":
            series["Date"] = series.Date.dt.to_timestamp()
        sales_line(series, 340)
    left, right = st.columns(2)
    with left, panel("Nhịp mùa vụ", "Doanh số trung bình / bộ phận / tuần, nhóm theo tháng"):
        monthly = data.groupby(["Year", "Month"], as_index=False).Weekly_Sales.mean()
        monthly["Year"] = monthly.Year.astype(str)
        fig = px.line(monthly, x="Month", y="Weekly_Sales", color="Year", markers=True)
        fig.update_xaxes(dtick=1)
        chart(fig)
    with right, panel("So sánh theo quý", "Doanh số trung bình / bộ phận / tuần"):
        quarters = data.groupby(["Year", "Quarter"], as_index=False).Weekly_Sales.mean()
        quarters["Period"] = quarters.Year.astype(str) + " · Q" + quarters.Quarter.astype(str)
        fig = px.bar(quarters, x="Period", y="Weekly_Sales", color_discrete_sequence=[NAVY])
        fig.update_xaxes(title=None)
        chart(fig)
    with panel("Loại cửa hàng qua các năm", "Doanh số trung bình / bộ phận / tuần; không phải tăng trưởng cùng kỳ"):
        yearly = data.groupby(["Year", "Type"], as_index=False).Weekly_Sales.mean()
        yearly.Year = yearly.Year.astype(str)
        chart(px.bar(yearly, x="Year", y="Weekly_Sales", color="Type", barmode="group", color_discrete_map=TYPE_COLORS), 290)


def correlation_page(data):
    factors = ["Temperature", "Unemployment", "Fuel_Price", "CPI"]
    insight("Tương quan không đồng nghĩa với quan hệ nhân quả", "Hệ số tính trên toàn bộ phạm vi. Biểu đồ điểm dùng tối đa 3.000 bản ghi cố định để giữ giao diện phản hồi nhanh.")
    sample = data.sample(min(3000, len(data)), random_state=42)
    for pair in (factors[:2], factors[2:]):
        for col, factor in zip(st.columns(2), pair):
            with col, panel(LABELS[factor], f"Pearson r = {data[factor].corr(data.Weekly_Sales):.3f} · doanh số / bộ phận / tuần"):
                fig = px.scatter(sample, x=factor, y="Weekly_Sales", color_discrete_sequence=[TEAL], opacity=.28)
                fig.update_traces(marker_size=5)
                chart(fig, 290)
    with panel("Diễn biến chỉ số kinh tế", "Trung bình theo cửa hàng / tuần trong từng tháng"):
        selected = st.selectbox("Chỉ số", factors, format_func=lambda x: LABELS[x], key="economic_factor")
        store_weeks = data.drop_duplicates(["Store", "Date"])
        series = store_weeks.groupby(store_weeks.Date.dt.to_period("M"))[selected].mean().reset_index()
        series.Date = series.Date.dt.to_timestamp()
        fig = px.line(series, x="Date", y=selected, color_discrete_sequence=[NAVY], markers=True)
        chart(fig, 270)


def holiday_analysis_page(data):
    groups = data.groupby("IsHoliday").Weekly_Sales.mean()
    regular, holiday = groups.get(False, np.nan), groups.get(True, np.nan)
    change = (holiday / regular - 1) * 100 if np.isfinite(regular) and regular != 0 else np.nan
    metrics([
        ("Doanh số tuần lễ", money(holiday), "Trung bình / bộ phận / tuần"),
        ("Doanh số tuần thường", money(regular), "Trung bình / bộ phận / tuần"),
        ("Chênh lệch tuần lễ", f"{change:+.1f}%" if np.isfinite(change) else "—", "So với tuần thường trong phạm vi"),
    ])
    view = data.assign(Holiday=data.IsHoliday.map({False: "Tuần thường", True: "Tuần lễ"}))
    left, right = st.columns(2)
    with left, panel("Phân phối doanh số", "Tứ phân vị toàn bộ dữ liệu; không vẽ điểm ngoại lệ"):
        chart(distribution_box(view, "Holiday"))
    with right, panel("Mức hưởng lợi theo loại cửa hàng", "Doanh số trung bình / bộ phận / tuần"):
        grouped = view.groupby(["Type", "Holiday"], as_index=False).Weekly_Sales.mean()
        fig = px.bar(grouped, x="Type", y="Weekly_Sales", color="Holiday", barmode="group",
                     color_discrete_map={"Tuần thường": NAVY, "Tuần lễ": TEAL})
        chart(fig)
    with panel("Cao điểm cuối năm", "Tuần ISO 45–52 · trung bình / bộ phận / tuần qua các năm được chọn"):
        end = data[data.Week.between(45, 52)]
        if end.empty:
            empty_state("Phạm vi đang chọn chưa có dữ liệu tuần 45–52. Hãy chọn thêm năm để xem cao điểm cuối năm.")
        else:
            pattern = end.groupby(["Week", "Type"], as_index=False).Weekly_Sales.mean()
            fig = px.line(pattern, x="Week", y="Weekly_Sales", color="Type", markers=True, color_discrete_map=TYPE_COLORS)
            fig.update_xaxes(dtick=1)
            chart(fig, 330)
    insight("Đọc đúng hiệu ứng ngày lễ", "Phân nhóm dựa trên cột IsHoliday của dữ liệu gốc. Chênh lệch là so sánh mô tả, chưa điều chỉnh khác biệt cửa hàng, bộ phận hay mùa vụ.")


def prediction_page(data, test_data):
    left, right = st.columns([1.2, 1])
    with left, panel("Thiết lập kịch bản", "Dự đoán doanh số cho một bộ phận trong một tuần"):
        store = st.selectbox("Cửa hàng", sorted(data.Store.unique()), format_func=lambda x: f"Cửa hàng {x:02d}", key="prediction_store")
        store_data = data[data.Store == store]
        store_info = store_data.iloc[0]
        st.caption(f"Loại {store_info.Type} · diện tích thực tế {store_info.Size:,.0f} ft²")
        with st.form("prediction_form"):
            c1, c2 = st.columns(2)
            with c1:
                dept = st.selectbox("Bộ phận", sorted(store_data.Dept.unique()), key="prediction_dept")
                years = sorted(set(data.Year) | set(test_data.Year))
                year = st.selectbox("Năm", years, index=years.index(int(data.Year.max())), key="prediction_year")
            with c2:
                week = st.slider("Tuần trong năm", 1, 52, 45, key="prediction_week")
                is_holiday = st.checkbox("Tuần ngày lễ", key="prediction_holiday")
            size = st.slider("Diện tích cửa hàng (ft²)", int(data.Size.min()), int(data.Size.max()), int(store_info.Size), key=f"prediction_size_{store}")
            submitted = st.form_submit_button("Tạo dự đoán  →", type="primary", width="stretch")
    with right, panel("Thông tin mô hình", "Gradient Boosting Regressor"):
        st.markdown("**12 đặc trưng đầu vào**")
        st.write("Cửa hàng, bộ phận, diện tích, loại cửa hàng, nhiệt độ, giá nhiên liệu, CPI, thất nghiệp, ngày lễ, năm, tháng và tuần.")
        insight("Sẵn sàng khi bạn cần", "Mô hình được huấn luyện ở lần tạo dự đoán đầu tiên và được lưu trong bộ nhớ để tái sử dụng. Lần đầu có thể mất vài phút.")
        st.caption("Các yếu tố kinh tế dùng trung bình lịch sử; tháng được ước lượng từ tuần. Đây là kịch bản tham khảo trên dữ liệu lịch sử.")
    if submitted:
        try:
            with st.spinner("Đang chuẩn bị mô hình và tính dự đoán…", show_time=True):
                model = train_model(data)
                row = pd.DataFrame({
                    "Store": [store], "Dept": [dept], "Size": [size],
                    "Type_encoded": [model.label_encoder.transform([store_info.Type])[0]],
                    "Temperature": [data.Temperature.mean()], "Fuel_Price": [data.Fuel_Price.mean()],
                    "CPI": [data.CPI.mean()], "Unemployment": [data.Unemployment.mean()],
                    "IsHoliday_encoded": [int(is_holiday)], "Year": [year],
                    "Month": [min((week - 1) // 4 + 1, 12)], "Week": [week],
                })
                prediction = float(model.predict(row[model.feature_names])[0])
                history = store_data[store_data.Dept == dept].Weekly_Sales.mean()
                st.session_state["prediction_result"] = {
                    "store": int(store), "dept": int(dept), "year": int(year), "week": int(week),
                    "holiday": is_holiday, "size": size, "prediction": prediction, "history": float(history),
                    "r2": float(model.validation_r2), "importance": model.feature_importances_,
                }
        except ImportError as exc:
            logging.getLogger(__name__).exception("Model dependency could not be loaded")
            if "Application Control" in str(exc):
                st.error("Windows đang chặn thư viện tính toán SciPy/scikit-learn nên mô hình chưa thể chạy. Cần quản trị thiết bị cho phép thư viện theo chính sách của máy; chạy lại notebook không khắc phục lỗi này.")
            else:
                st.error("Chưa thể tải thư viện huấn luyện scikit-learn. Hãy kiểm tra cài đặt và quyền chạy thư viện của môi trường Python.")
            with st.expander("Kiểm tra môi trường chạy"):
                st.code("python run_project.py doctor", language="powershell")
                st.caption("Dashboard tự huấn luyện khi tạo dự đoán, không cần chạy notebook trước.")
            return
        except Exception:
            logging.getLogger(__name__).exception("Prediction failed")
            st.error("Chưa thể tạo dự đoán. Vui lòng kiểm tra dữ liệu đầu vào hoặc thử lại.")
            return
    result = st.session_state.get("prediction_result")
    if result is None:
        with panel("Kết quả dự đoán", "Kết quả sẽ xuất hiện ở đây sau khi bạn gửi kịch bản"):
            st.caption("Chọn cửa hàng và bộ phận, sau đó bấm “Tạo dự đoán”.")
        return
    with panel("Kịch bản đã tính", f"Cửa hàng {result['store']} · Bộ phận {result['dept']} · Tuần {result['week']}/{result['year']} · {'Tuần lễ' if result['holiday'] else 'Tuần thường'} · {result['size']:,} ft²"):
        st.caption("Kết quả giữ nguyên theo kịch bản đã gửi. Bấm tạo dự đoán để áp dụng thay đổi trong biểu mẫu.")
        metrics([
            ("Doanh số dự đoán", money(result["prediction"]), "Một bộ phận / tuần"),
            ("Trung bình lịch sử", money(result["history"]), "Cùng cửa hàng và bộ phận"),
            ("Chênh lệch", money(result["prediction"] - result["history"]), "Dự đoán trừ trung bình lịch sử"),
        ])
        st.caption(f"R² validation: {result['r2']:.3f} · chia ngẫu nhiên 80/20; không phải đánh giá dự báo theo thời gian.")
    with panel("Các đặc trưng quan trọng", "Mức độ quan trọng trong mô hình; không biểu thị quan hệ nhân quả"):
        names = {**LABELS, "Type_encoded": "Loại cửa hàng", "IsHoliday_encoded": "Ngày lễ"}
        values = pd.Series(result["importance"], index=[names.get(x, x) for x in MODEL_FEATURES]).nlargest(10).sort_values()
        fig = go.Figure(go.Bar(x=values.values, y=values.index, orientation="h", marker_color=TEAL))
        fig.update_xaxes(tickformat=".0%")
        chart(fig, 320, horizontal=True)


def store_performance_page(data):
    # Store/week totals avoid comparing a department average against whole-store area.
    per_week = data.groupby(["Store", "Date"], as_index=False).Weekly_Sales.sum()
    performance = per_week.groupby("Store").agg(Total_Sales=("Weekly_Sales", "sum"), Avg_Weekly=("Weekly_Sales", "mean"), Weeks=("Date", "nunique")).reset_index()
    performance = performance.merge(data[["Store", "Size", "Type"]].drop_duplicates("Store"), on="Store")
    performance["Sales_per_sqft"] = performance.Avg_Weekly / performance.Size * 1000
    best = performance.loc[performance.Total_Sales.idxmax()]
    metrics([
        ("Cửa hàng dẫn đầu", f"#{int(best.Store):02d}", f"{money(best.Total_Sales, True)} tổng doanh số"),
        ("Cửa hàng đang so sánh", len(performance), "Trong phạm vi bộ lọc"),
        ("TB doanh số / cửa hàng / tuần", money(per_week.Weekly_Sales.mean(), True), "Tổng các bộ phận mỗi cửa hàng"),
    ])
    left, right = st.columns(2)
    with left, panel("10 cửa hàng dẫn đầu", "Xếp hạng theo tổng doanh số trong kỳ"):
        ranked_bar(performance.set_index("Store").Total_Sales.nlargest(10), "Cửa hàng", height=340)
    with right, panel("Hiệu suất diện tích", "Doanh số trung bình toàn cửa hàng / tuần trên 1.000 ft²"):
        fig = px.scatter(performance, x="Size", y="Sales_per_sqft", color="Type", hover_name="Store", color_discrete_map=TYPE_COLORS)
        fig.update_traces(marker_size=13, marker_opacity=.85, marker_line_color="white", marker_line_width=1)
        fig.update_yaxes(title="USD / tuần / 1.000 ft²")
        chart(fig, 340)
    with panel("Bảng hiệu suất cửa hàng", "Bấm vào tiêu đề cột để sắp xếp; xuất bảng bằng nút bên dưới"):
        ordered = performance.sort_values("Total_Sales", ascending=False)
        st.dataframe(ordered, hide_index=True, width="stretch", column_config={
            "Store": "Cửa hàng", "Type": "Loại", "Size": st.column_config.NumberColumn("Diện tích (ft²)", format="%d"),
            "Total_Sales": st.column_config.NumberColumn("Tổng doanh số", format="$%.0f"),
            "Avg_Weekly": st.column_config.NumberColumn("TB / cửa hàng / tuần", format="$%.0f"),
            "Weeks": "Số tuần", "Sales_per_sqft": st.column_config.NumberColumn("USD / tuần / 1.000 ft²", format="$%.2f"),
        })
        st.download_button("Tải bảng CSV", ordered.to_csv(index=False).encode("utf-8-sig"), "walmart_store_performance.csv", "text/csv")
    with panel("Khám phá từng cửa hàng", "10 bộ phận có tổng doanh số cao nhất tại cửa hàng được chọn"):
        store = st.selectbox("Cửa hàng", sorted(data.Store.unique()), key="detail_store")
        part = data[data.Store == store]
        a, b = st.columns(2)
        totals = part.groupby("Dept").Weekly_Sales.sum().nlargest(10)
        with a:
            st.caption("TỔNG DOANH SỐ")
            ranked_bar(totals, "Bộ phận")
        with b:
            st.caption("TRUNG BÌNH / TUẦN")
            ranked_bar(part.groupby("Dept").Weekly_Sales.mean().reindex(totals.index), "Bộ phận", NAVY)


def main():
    setup_ui()
    try:
        data, test_data = load_data()
    except (OSError, ValueError, KeyError):
        st.error("Không thể đọc bộ dữ liệu. Vui lòng kiểm tra bốn file CSV trong Do_An/dataset.")
        st.stop()
    # Keep filter values when their widgets are absent on the prediction page.
    for key in ("filter_types", "filter_years", "filter_month"):
        if key in st.session_state:
            st.session_state[key] = st.session_state[key]
    page = sidebar()
    heading = st.empty()
    if page == "Dự đoán doanh số":
        with heading:
            page_header(PAGES[page][1], PAGES[page][2], data)
        st.caption("Dự đoán sử dụng toàn bộ dữ liệu huấn luyện. Chọn kịch bản trong biểu mẫu bên dưới.")
        prediction_page(data, test_data)
    else:
        filtered = filter_bar(data)
        with heading:
            page_header(PAGES[page][1], PAGES[page][2], filtered)
        handlers = {
            "Tổng quan": overview_page, "Khám phá dữ liệu": eda_page,
            "Xu hướng thời gian": time_analysis_page, "Yếu tố tác động": correlation_page,
            "Ngày lễ & mùa vụ": holiday_analysis_page, "Hiệu suất cửa hàng": store_performance_page,
        }
        if not filtered.empty:
            handlers[page](filtered)
        else:
            empty_state("Không có dữ liệu phù hợp. Hãy đổi loại cửa hàng, năm, tháng hoặc đặt lại bộ lọc.")
    st.markdown('<div class="footer"><span>WALMART · SALES INTELLIGENCE</span><span>Dữ liệu lịch sử · Đơn vị USD · Đồ án phân tích dữ liệu</span></div>', unsafe_allow_html=True)
    scroll_to_top_on_navigation(page)


if __name__ == "__main__":
    main()
