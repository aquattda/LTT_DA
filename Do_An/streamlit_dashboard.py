import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
import os
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Walmart Sales Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 2rem;
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .metric-card {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    .insight-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-left: 5px solid #007bff;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and prepare data"""
    try:
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        dataset_dir = os.path.join(current_dir, "dataset")
        
        # Load datasets with proper path handling
        train_df = pd.read_csv(os.path.join(dataset_dir, "train.csv"))
        stores_df = pd.read_csv(os.path.join(dataset_dir, "stores.csv"))
        features_df = pd.read_csv(os.path.join(dataset_dir, "features.csv"))
        test_df = pd.read_csv(os.path.join(dataset_dir, "test.csv"))
        
        # Merge data for training set
        train_stores = pd.merge(train_df, stores_df, on='Store', how='left')
        walmart_data = pd.merge(train_stores, features_df, on=['Store', 'Date', 'IsHoliday'], how='left')
        
        # Merge data for test set
        test_stores = pd.merge(test_df, stores_df, on='Store', how='left')
        test_data = pd.merge(test_stores, features_df, on=['Store', 'Date', 'IsHoliday'], how='left')
        
        # Process dates
        walmart_data['Date'] = pd.to_datetime(walmart_data['Date'])
        test_data['Date'] = pd.to_datetime(test_data['Date'])
        
        # Add time features
        for df in [walmart_data, test_data]:
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.month
            df['Week'] = df['Date'].dt.isocalendar().week
            df['Quarter'] = df['Date'].dt.quarter
            
        # Fill missing values
        markdown_cols = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']
        walmart_data[markdown_cols] = walmart_data[markdown_cols].fillna(0)
        test_data[markdown_cols] = test_data[markdown_cols].fillna(0)
        test_data[['CPI', 'Unemployment']] = test_data[['CPI', 'Unemployment']].fillna(0)
        
        return walmart_data, test_data
    
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.error(f"Current working directory: {os.getcwd()}")
        st.error(f"Script directory: {os.path.dirname(os.path.abspath(__file__))}")
        st.error(f"Looking for dataset in: {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset')}")
        
        # List available files
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            st.error(f"Files in script directory: {os.listdir(current_dir)}")
            if os.path.exists(os.path.join(current_dir, 'dataset')):
                st.error(f"Files in dataset directory: {os.listdir(os.path.join(current_dir, 'dataset'))}")
        except:
            pass
            
        return None, None

@st.cache_resource
def load_model():
    """Load the trained model"""
    try:
        model = joblib.load('rf_walmart_model.pkl')
        return model
    except:
        st.warning("Không tìm thấy file mô hình. Chức năng dự đoán sẽ bị vô hiệu hóa.")
        return None

def main():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<h1 class="main-header">Walmart Sales Analysis Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    walmart_data, test_data = load_data()
    if walmart_data is None:
        st.error("Không thể tải dữ liệu. Vui lòng kiểm tra xem các file dataset có tồn tại không.")
        return
    
    # Sidebar
    st.sidebar.title("Điều Hướng")
    page = st.sidebar.selectbox(
        "Chọn một trang:",
        ["Overview", "EDA", "Phân Tích Thời Gian", "Phân Tích Tương Quan", 
         "Phân Tích Ngày Lễ", "Dự Đoán", "Hiệu Suất Cửa Hàng"]
    )
    
    if page == "Overview":
        overview_page(walmart_data)
    elif page == "EDA":
        eda_page(walmart_data)
    elif page == "Phân Tích Thời Gian":
        time_analysis_page(walmart_data)
    elif page == "Phân Tích Tương Quan":
        correlation_page(walmart_data)
    elif page == "Phân Tích Ngày Lễ":
        holiday_analysis_page(walmart_data)
    elif page == "Dự Đoán":
        prediction_page(walmart_data, test_data)
    elif page == "Hiệu Suất Cửa Hàng":
        store_performance_page(walmart_data)

def overview_page(walmart_data):
    st.markdown('<h2 class="sub-header">Tổng Quan Kinh Doanh</h2>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    total_sales = walmart_data['Weekly_Sales'].sum()
    avg_sales = walmart_data['Weekly_Sales'].mean()
    total_stores = walmart_data['Store'].nunique()
    total_departments = walmart_data['Dept'].nunique()
    
    with col1:
        st.metric("Tổng Doanh Số", f"${total_sales:,.0f}")
    with col2:
        st.metric("Doanh Số Trung Bình Hàng Tuần", f"${avg_sales:,.0f}")
    with col3:
        st.metric("Tổng Số Cửa Hàng", f"{total_stores}")
    with col4:
        st.metric("Tổng Số Bộ Phận", f"{total_departments}")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales by store type
        type_sales = walmart_data.groupby('Type')['Weekly_Sales'].agg(['mean', 'sum']).reset_index()
        fig = px.bar(type_sales, x='Type', y='mean', 
                     title='Average Weekly Sales by Store Type',
                     labels={'mean': 'Average Sales ($)', 'Type': 'Store Type'},
                     color='Type', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Store distribution
        store_counts = walmart_data['Type'].value_counts()
        fig = px.pie(values=store_counts.values, names=store_counts.index,
                     title='Phân Phối Loại Cửa Hàng',
                     color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig, use_container_width=True)
    
    # Top performing departments
    st.markdown('<h3 class="sub-header">Top 10 Bộ Phận Theo Doanh Số</h3>', unsafe_allow_html=True)
    dept_sales = walmart_data.groupby('Dept')['Weekly_Sales'].mean().sort_values(ascending=False).head(10)
    fig = px.bar(x=dept_sales.index.astype(str), y=dept_sales.values,
                 title='Top 10 Bộ Phận Theo Doanh Số Trung Bình Hàng Tuần',
                 labels={'x': 'Bộ Phận', 'y': 'Doanh Số Trung Bình ($)'},
                 color=dept_sales.values, color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)
    
    # Insights
    st.markdown("### Những Phát Hiện Quan Trọng:")
    st.markdown(f"""
    - **Loại Cửa Hàng A** có doanh số trung bình cao nhất (${walmart_data[walmart_data['Type'] == 'A']['Weekly_Sales'].mean():,.0f})
    - **Bộ Phận {dept_sales.index[0]}** là bộ phận hoạt động tốt nhất với doanh số trung bình hàng tuần ${dept_sales.iloc[0]:,.0f}
    - Tổng cộng có **{total_stores} cửa hàng** trải rộng trên **{total_departments} bộ phận**
    - **{walmart_data['Type'].value_counts()['A']} cửa hàng** thuộc Loại A (định dạng lớn nhất)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def eda_page(walmart_data):
    st.markdown('<h2 class="sub-header">Phân Tích Thăm Dò Dữ Liệu</h2>', unsafe_allow_html=True)
    
    # Interactive filters
    st.sidebar.markdown("### Bộ Lọc")
    selected_types = st.sidebar.multiselect("Loại Cửa Hàng", 
                                           options=walmart_data['Type'].unique(),
                                           default=walmart_data['Type'].unique())
    
    selected_years = st.sidebar.multiselect("Năm",
                                          options=walmart_data['Year'].unique(),
                                          default=walmart_data['Year'].unique())
    
    # Filter data
    filtered_data = walmart_data[
        (walmart_data['Type'].isin(selected_types)) &
        (walmart_data['Year'].isin(selected_years))
    ]
    
    # Store size analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Store size vs sales
        store_size_sales = filtered_data.groupby('Store').agg({
            'Size': 'first',
            'Weekly_Sales': 'mean',
            'Type': 'first'
        }).reset_index()
        
        fig = px.scatter(store_size_sales, x='Size', y='Weekly_Sales', 
                        color='Type', size='Weekly_Sales',
                        title='Kích Cỡ Cửa Hàng vs Doanh Số Trung Bình Hàng Tuần',
                        labels={'Size': 'Kích Cỡ Cửa Hàng (feet vuông)', 'Weekly_Sales': 'Doanh Số TB Hàng Tuần ($)'},
                        hover_data=['Store'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Sales distribution
        fig = px.histogram(filtered_data, x='Weekly_Sales', nbins=50,
                          title='Phân Phối Doanh Số Hàng Tuần',
                          labels={'Weekly_Sales': 'Doanh Số Hàng Tuần ($)', 'count': 'Tần Suất'},
                          color_discrete_sequence=['skyblue'])
        fig.add_vline(x=filtered_data['Weekly_Sales'].mean(), 
                      annotation_text=f"Trung bình: ${filtered_data['Weekly_Sales'].mean():,.0f}",
                      line_dash="dash", line_color="red")
        st.plotly_chart(fig, use_container_width=True)
    
    # Department analysis
    st.markdown('<h3 class="sub-header">Phân Tích Bộ Phận</h3>', unsafe_allow_html=True)
    
    dept_analysis = filtered_data.groupby(['Dept', 'Type'])['Weekly_Sales'].mean().reset_index()
    fig = px.box(filtered_data, x='Type', y='Weekly_Sales',
                 title='Phân Phối Doanh Số Theo Loại Cửa Hàng',
                 labels={'Weekly_Sales': 'Doanh Số Hàng Tuần ($)', 'Type': 'Loại Cửa Hàng'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation heatmap
    st.markdown('<h3 class="sub-header">Bản Đồ Nhiệt Tương Quan</h3>', unsafe_allow_html=True)
    numeric_cols = ['Weekly_Sales', 'Size', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    corr_data = filtered_data[numeric_cols].corr()
    
    fig = px.imshow(corr_data, text_auto=True, aspect="auto",
                    title='Ma Trận Tương Quan Các Biến Số Chính',
                    color_continuous_scale='RdBu_r')
    st.plotly_chart(fig, use_container_width=True)

def time_analysis_page(walmart_data):
    st.markdown('<h2 class="sub-header">Phân Tích Dãy Thời Gian</h2>', unsafe_allow_html=True)
    
    # Monthly sales trend
    monthly_sales = walmart_data.groupby(['Year', 'Month'])['Weekly_Sales'].sum().reset_index()
    monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(day=1))
    
    fig = px.line(monthly_sales, x='Date', y='Weekly_Sales',
                  title='Xu Hướng Doanh Số Theo Tháng (2010-2012)',
                  labels={'Weekly_Sales': 'Tổng Doanh Số ($)', 'Date': 'Tháng'},
                  markers=True)
    
    # Add holiday markers using shapes instead
    holiday_months = [(2010, 11), (2010, 12), (2011, 11), (2011, 12), (2012, 11)]
    for year, month in holiday_months:
        holiday_date = f"{year}-{month:02d}-01"
        fig.add_shape(
            type="line",
            x0=holiday_date, x1=holiday_date,
            y0=0, y1=1,
            yref="paper",
            line=dict(color="red", width=2, dash="dash")
        )
        fig.add_annotation(
            x=holiday_date,
            y=1.05,
            yref="paper",
            text=f"Ngày Lễ {year}-{month:02d}",
            showarrow=False,
            font=dict(color="red", size=10),
            textangle=-45
        )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Weekly patterns
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales by quarter
        quarterly_sales = walmart_data.groupby(['Year', 'Quarter'])['Weekly_Sales'].mean().reset_index()
        quarterly_sales['Period'] = quarterly_sales['Year'].astype(str) + '-Q' + quarterly_sales['Quarter'].astype(str)
        
        fig = px.bar(quarterly_sales, x='Period', y='Weekly_Sales',
                     title='Doanh Số Trung Bình Theo Quý',
                     labels={'Weekly_Sales': 'Doanh Số Trung Bình ($)', 'Period': 'Quý'},
                     color='Weekly_Sales', color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Seasonal analysis
        walmart_data['Season'] = walmart_data['Month'].map({
            12: 'Mùa Đông', 1: 'Mùa Đông', 2: 'Mùa Đông',
            3: 'Mùa Xuân', 4: 'Mùa Xuân', 5: 'Mùa Xuân',
            6: 'Mùa Hè', 7: 'Mùa Hè', 8: 'Mùa Hè',
            9: 'Mùa Thu', 10: 'Mùa Thu', 11: 'Mùa Thu'
        })
        
        seasonal_sales = walmart_data.groupby('Season')['Weekly_Sales'].mean()
        fig = px.bar(x=seasonal_sales.index, y=seasonal_sales.values,
                     title='Doanh Số Trung Bình Theo Mùa',
                     labels={'x': 'Mùa', 'y': 'Doanh Số Trung Bình ($)'},
                     color=seasonal_sales.values, color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)
    
    # Year-over-year comparison
    st.markdown('<h3 class="sub-header">So Sánh Theo Năm</h3>', unsafe_allow_html=True)
    
    yearly_comparison = walmart_data.groupby(['Year', 'Type'])['Weekly_Sales'].mean().reset_index()
    fig = px.bar(yearly_comparison, x='Year', y='Weekly_Sales', color='Type',
                 title='Doanh Số Trung Bình Theo Năm và Loại Cửa Hàng',
                 labels={'Weekly_Sales': 'Doanh Số Trung Bình ($)', 'Year': 'Năm'},
                 barmode='group')
    st.plotly_chart(fig, use_container_width=True)

def correlation_page(walmart_data):
    st.markdown('<h2 class="sub-header">Phân Tích Tương Quan</h2>', unsafe_allow_html=True)
    
    # Economic factors analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Temperature vs Sales
        temp_corr = walmart_data[['Temperature', 'Weekly_Sales']].corr().iloc[0, 1]
        
        fig = px.scatter(walmart_data.sample(5000), x='Temperature', y='Weekly_Sales',
                        title=f'Nhiệt Độ vs Doanh Số (Tương quan: {temp_corr:.3f})',
                        labels={'Temperature': 'Nhiệt Độ (°F)', 'Weekly_Sales': 'Doanh Số Hàng Tuần ($)'},
                        trendline="ols", opacity=0.6)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Unemployment vs Sales
        unemp_corr = walmart_data[['Unemployment', 'Weekly_Sales']].corr().iloc[0, 1]
        
        fig = px.scatter(walmart_data.sample(5000), x='Unemployment', y='Weekly_Sales',
                        title=f'Tỷ Lệ Thất Nghiệp vs Doanh Số (Tương quan: {unemp_corr:.3f})',
                        labels={'Unemployment': 'Tỷ Lệ Thất Nghiệp (%)', 'Weekly_Sales': 'Doanh Số Hàng Tuần ($)'},
                        trendline="ols", opacity=0.6)
        st.plotly_chart(fig, use_container_width=True)
    
    # Fuel price analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Fuel Price vs Sales
        fuel_corr = walmart_data[['Fuel_Price', 'Weekly_Sales']].corr().iloc[0, 1]
        
        fig = px.scatter(walmart_data.sample(5000), x='Fuel_Price', y='Weekly_Sales',
                        title=f'Giá Nhiên Liệu vs Doanh Số (Tương quan: {fuel_corr:.3f})',
                        labels={'Fuel_Price': 'Giá Nhiên Liệu ($/gallon)', 'Weekly_Sales': 'Doanh Số Hàng Tuần ($)'},
                        trendline="ols", opacity=0.6)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # CPI vs Sales
        cpi_corr = walmart_data[['CPI', 'Weekly_Sales']].corr().iloc[0, 1]
        
        fig = px.scatter(walmart_data.sample(5000), x='CPI', y='Weekly_Sales',
                        title=f'CPI vs Doanh Số (Tương quan: {cpi_corr:.3f})',
                        labels={'CPI': 'Chỉ Số Giá Tiêu Dùng', 'Weekly_Sales': 'Doanh Số Hàng Tuần ($)'},
                        trendline="ols", opacity=0.6)
        st.plotly_chart(fig, use_container_width=True)
    
    # Economic factors over time
    st.markdown('<h3 class="sub-header">Các Yếu Tố Kinh Tế Theo Thời Gian</h3>', unsafe_allow_html=True)
    
    # Time series of economic indicators
    monthly_econ = walmart_data.groupby(['Year', 'Month']).agg({
        'Temperature': 'mean',
        'Fuel_Price': 'mean',
        'CPI': 'mean',
        'Unemployment': 'mean',
        'Weekly_Sales': 'sum'
    }).reset_index()
    monthly_econ['Date'] = pd.to_datetime(monthly_econ[['Year', 'Month']].assign(day=1))
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Nhiệt Độ', 'Giá Nhiên Liệu', 'CPI', 'Tỷ Lệ Thất Nghiệp'),
        specs=[[{"secondary_y": True}, {"secondary_y": True}],
               [{"secondary_y": True}, {"secondary_y": True}]]
    )
    
    # Add traces
    factors = ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    colors = ['red', 'green', 'blue', 'orange']
    positions = [(1, 1), (1, 2), (2, 1), (2, 2)]
    
    for factor, color, (row, col) in zip(factors, colors, positions):
        # Economic factor
        fig.add_trace(
            go.Scatter(x=monthly_econ['Date'], y=monthly_econ[factor], 
                      name=factor, line_color=color),
            row=row, col=col
        )
        
        # Sales on secondary y-axis
        fig.add_trace(
            go.Scatter(x=monthly_econ['Date'], y=monthly_econ['Weekly_Sales'],
                      name='Sales', line_color='white', opacity=0.8),
            row=row, col=col, secondary_y=True
        )
    
    fig.update_layout(height=600, showlegend=False, title_text="Các Yếu Tố Kinh Tế vs Doanh Số Theo Thời Gian")
    st.plotly_chart(fig, use_container_width=True)

def holiday_analysis_page(walmart_data):
    st.markdown('<h2 class="sub-header">Phân Tích Ngày Lễ</h2>', unsafe_allow_html=True)
    
    # Holiday vs Non-Holiday comparison
    holiday_stats = walmart_data.groupby('IsHoliday')['Weekly_Sales'].agg(['mean', 'median', 'std', 'count'])
    holiday_stats.index = ['Ngày Thường', 'Ngày Lễ']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Doanh Số TB Ngày Thường", f"${holiday_stats.loc['Ngày Thường', 'mean']:,.0f}")
    with col2:
        st.metric("Doanh Số TB Ngày Lễ", f"${holiday_stats.loc['Ngày Lễ', 'mean']:,.0f}")
    with col3:
        diff_pct = ((holiday_stats.loc['Ngày Lễ', 'mean'] - holiday_stats.loc['Ngày Thường', 'mean']) / 
                    holiday_stats.loc['Ngày Thường', 'mean'] * 100)
        st.metric("Tăng Trưởng Ngày Lễ", f"{diff_pct:+.1f}%")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Holiday vs Non-Holiday sales
        fig = px.box(walmart_data, x='IsHoliday', y='Weekly_Sales',
                     title='Phân Phối Doanh Số: Ngày Lễ vs Ngày Thường',
                     labels={'IsHoliday': 'Tuần Ngày Lễ', 'Weekly_Sales': 'Doanh Số Hàng Tuần ($)'})
        fig.update_xaxes(tickvals=[False, True], ticktext=['Ngày Thường', 'Ngày Lễ'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Holiday sales by store type
        holiday_type = walmart_data.groupby(['Type', 'IsHoliday'])['Weekly_Sales'].mean().reset_index()
        fig = px.bar(holiday_type, x='Type', y='Weekly_Sales', color='IsHoliday',
                     title='Doanh Số Ngày Lễ Theo Loại Cửa Hàng',
                     labels={'Weekly_Sales': 'Doanh Số Trung Bình ($)', 'Type': 'Loại Cửa Hàng'},
                     barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
    # End of year analysis
    st.markdown('<h3 class="sub-header">Phân Tích Cuối Năm</h3>', unsafe_allow_html=True)
    
    # Identify end of year weeks (Thanksgiving and Christmas)
    walmart_data['Is_EndOfYear'] = (
        ((walmart_data['Month'] == 11) & (walmart_data['Week'].isin([47, 48]))) |
        ((walmart_data['Month'] == 12) & (walmart_data['Week'].isin([51, 52])))
    )
    
    # Weekly sales pattern for end of year
    end_year_weeks = walmart_data[walmart_data['Week'].isin(range(45, 53))]
    weekly_pattern = end_year_weeks.groupby(['Week', 'Type'])['Weekly_Sales'].mean().reset_index()
    
    fig = px.line(weekly_pattern, x='Week', y='Weekly_Sales', color='Type',
                  title='Doanh Số Cuối Năm (Tuần 45-52)',
                  labels={'Weekly_Sales': 'Doanh Số Trung Bình ($)', 'Week': 'Tuần Trong Năm'},
                  markers=True)
    
    # Add vertical lines for holidays
    fig.add_vline(x=47, line_dash="dash", annotation_text="Lễ Tạ Ơn")
    fig.add_vline(x=51, line_dash="dash", annotation_text="Giáng Sinh")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Holiday insights
    st.markdown("### Những Hiểu Biết Về Ngày Lễ:")
    thanksgiving_sales = walmart_data[walmart_data['Week'].isin([47, 48])]['Weekly_Sales'].mean()
    christmas_sales = walmart_data[walmart_data['Week'].isin([51, 52])]['Weekly_Sales'].mean()
    
    st.markdown(f"""
    - Các tuần ngày lễ cho thấy doanh số cao hơn **{diff_pct:+.1f}%** so với các tuần thường
    - **Giai đoạn Lễ Tạ Ơn** (Tuần 47-48): ${thanksgiving_sales:,.0f} doanh số trung bình
    - **Giai đoạn Giáng Sinh** (Tuần 51-52): ${christmas_sales:,.0f} doanh số trung bình
    - **{'Giáng Sinh' if christmas_sales > thanksgiving_sales else 'Lễ Tạ Ơn'}** cho thấy doanh số cao hơn
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def prediction_page(walmart_data, test_data):
    st.markdown('<h2 class="sub-header">Dự Đoán Doanh Số</h2>', unsafe_allow_html=True)
    
    model = load_model()
    
    if model is None:
        st.error("Mô hình không khả dụng. Vui lòng đảm bảo file 'rf_walmart_model.pkl' tồn tại.")
        return
    
    # Prediction interface
    st.markdown("### Tham Số Dự Đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        store = st.selectbox("Cửa Hàng", options=sorted(walmart_data['Store'].unique()))
        dept = st.selectbox("Bộ Phận", options=sorted(walmart_data['Dept'].unique()))
        is_holiday = st.checkbox("Là Tuần Ngày Lễ")
    
    with col2:
        year = st.selectbox("Năm", options=[2010, 2011, 2012, 2013], index=2)
        week = st.slider("Tuần trong năm", min_value=1, max_value=52, value=45)
        size = st.slider("Kích Cỡ Cửa Hàng (feet vuông)", 
                        min_value=float(walmart_data['Size'].min()),
                        max_value=float(walmart_data['Size'].max()),
                        value=float(walmart_data['Size'].mean()))
    
    # Get store type from selected store (for Types encoding)
    store_type = walmart_data[walmart_data['Store'] == store]['Type'].iloc[0]
    
    # Auto-calculate dependent values
    month = ((week - 1) // 4) + 1  # Estimate month from week
    if month > 12:
        month = 12
    quarter = ((month - 1) // 3) + 1
    
    # Prepare prediction data with exact column names from trained model
    pred_data = pd.DataFrame({
        'Store': [store],
        'Dept': [dept],
        'IsHoliday': [1 if is_holiday else 0],
        'Size': [size],
        'Temperature': [walmart_data['Temperature'].mean()],  # Use average
        'Year': [year],
        'Month': [month],
        'Week': [week],
        'Quarter': [quarter],
        'Types': [1 if store_type == 'A' else 2 if store_type == 'B' else 3],
        'Fuel_Price_mean': [walmart_data['Fuel_Price'].mean()],
        'CPI_mean': [walmart_data['CPI'].mean()],
        'Tem_mean': [walmart_data['Temperature'].mean()],
        'Unem_mean': [walmart_data['Unemployment'].mean()]
    })
    
    if st.button("Dự Đoán Doanh Số", type="primary"):
        try:
            # Debug: Show model feature names if available
            # if hasattr(model, 'feature_names_in_'):
            #     st.write("Model feature names:", model.feature_names_in_)
            #     st.write("Prediction data columns:", pred_data.columns.tolist())
                
            # Try to match column names exactly
            if hasattr(model, 'feature_names_in_'):
                expected_features = model.feature_names_in_
                current_features = pred_data.columns.tolist()
                
                # Check for missing features
                missing_features = [f for f in expected_features if f not in current_features]
                if missing_features:
                    st.error(f"Missing features: {missing_features}")
                    return
                
                # Reorder columns to match expected order
                pred_data = pred_data[expected_features]
            
            prediction = model.predict(pred_data)[0]
            
            st.success(f"### Dự Đoán Doanh Số Hàng Tuần: ${prediction:,.2f}")
            
            # Compare with historical data
            historical_data = walmart_data[
                (walmart_data['Store'] == store) & 
                (walmart_data['Dept'] == dept)
            ]['Weekly_Sales']
            
            if len(historical_data) > 0:
                hist_mean = historical_data.mean()
                hist_std = historical_data.std()
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Trung Bình Lịch Sử", f"${hist_mean:,.2f}")
                with col2:
                    st.metric("Chênh Lệch Từ Trung Bình", 
                             f"${prediction - hist_mean:+,.2f}")
                # with col3:
                #     if hist_std > 0:
                #         z_score = (prediction - hist_mean) / hist_std
                #         st.metric("Z-Score", f"{z_score:.2f}")
        
        except Exception as e:
            st.error(f"Lỗi dự đoán: {e}")
    
    # Model performance
    st.markdown("### Hiệu Suất Mô Hình")
    
    # Display model info
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Loại Mô Hình:** Random Forest Regressor
        
        **Các Đặc Trưng Sử Dụng:**
        - ID Cửa Hàng và Bộ Phận
        - Đặc điểm cửa hàng (Loại, Kích thước)
        - Các yếu tố kinh tế (Nhiệt độ, Giá nhiên liệu, CPI, Thất nghiệp)
        - Đặc trưng thời gian (Năm, Tháng, Tuần, Quý)
        - Chỉ số ngày lễ
        - Các đặc trưng giảm giá
        """)
    
    with col2:
        # Feature importance (if available)
        if hasattr(model, 'feature_importances_'):
            feature_names = pred_data.columns
            importance_df = pd.DataFrame({
                'feature': feature_names,
                'importance': model.feature_importances_
            }).sort_values('importance', ascending=False).head(10)
            
            fig = px.bar(importance_df, x='importance', y='feature',
                        title='Top 10 Mức Độ Quan Trọng Của Đặc Trưng',
                        labels={'importance': 'Mức Độ Quan Trọng', 'feature': 'Đặc Trưng'},
                        orientation='h')
            st.plotly_chart(fig, use_container_width=True)

def store_performance_page(walmart_data):
    st.markdown('<h2 class="sub-header">Phân Tích Hiệu Suất Cửa Hàng</h2>', unsafe_allow_html=True)
    
    # Store performance metrics
    store_performance = walmart_data.groupby('Store').agg({
        'Weekly_Sales': ['sum', 'mean', 'std'],
        'Size': 'first',
        'Type': 'first'
    }).round(2)
    
    store_performance.columns = ['Total_Sales', 'Avg_Sales', 'Sales_Std', 'Size', 'Type']
    store_performance = store_performance.reset_index()
    store_performance['Sales_per_sqft'] = store_performance['Avg_Sales'] / store_performance['Size'] * 1000
    
    # Top performing stores
    col1, col2 = st.columns(2)
    
    with col1:
        top_stores = store_performance.nlargest(10, 'Total_Sales')
        fig = px.bar(top_stores, x='Store', y='Total_Sales', color='Type',
                     title='Top 10 Cửa Hàng Theo Tổng Doanh Số',
                     labels={'Total_Sales': 'Tổng Doanh Số ($)', 'Store': 'ID Cửa Hàng'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Sales per square foot
        fig = px.scatter(store_performance, x='Size', y='Sales_per_sqft', 
                        color='Type', size='Total_Sales',
                        title='Hiệu Quả Doanh Số (Doanh số/1000 feet vuông)',
                        labels={'Size': 'Kích Cỡ Cửa Hàng (feet vuông)', 
                               'Sales_per_sqft': 'Doanh Số/1000 feet vuông ($)'},
                        hover_data=['Store'])
        st.plotly_chart(fig, use_container_width=True)
    
    # Store comparison table
    st.markdown("### Bảng Hiệu Suất Cửa Hàng")
    
    # Add filters
    type_filter = st.multiselect("Lọc theo Loại", 
                                options=store_performance['Type'].unique(),
                                default=store_performance['Type'].unique())
    
    filtered_stores = store_performance[store_performance['Type'].isin(type_filter)]
    
    # Display table
    st.dataframe(
        filtered_stores.sort_values('Total_Sales', ascending=False),
        use_container_width=True,
        column_config={
            "Store": "ID Cửa Hàng",
            "Total_Sales": st.column_config.NumberColumn("Tổng Doanh Số", format="$%.0f"),
            "Avg_Sales": st.column_config.NumberColumn("Doanh Số TB", format="$%.0f"),
            "Sales_Std": st.column_config.NumberColumn("Độ Lệch Chuẩn", format="$%.0f"),
            "Size": st.column_config.NumberColumn("Kích Thước (feet vuông)", format="%.0f"),
            "Sales_per_sqft": st.column_config.NumberColumn("Doanh Số/1000 feet vuông", format="$%.2f")
        }
    )
    
    # Department performance by store
    st.markdown("### Hiệu Suất Bộ Phận Theo Cửa Hàng")
    
    selected_store = st.selectbox("Chọn Cửa Hàng Để Phân Tích Bộ Phận", 
                                 options=sorted(walmart_data['Store'].unique()))
    
    store_dept_data = walmart_data[walmart_data['Store'] == selected_store]
    dept_performance = store_dept_data.groupby('Dept')['Weekly_Sales'].agg(['sum', 'mean', 'count']).reset_index()
    dept_performance.columns = ['Dept', 'Total_Sales', 'Avg_Sales', 'Weeks']
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top departments in selected store
        top_depts = dept_performance.nlargest(10, 'Total_Sales')
        fig = px.bar(top_depts, x='Dept', y='Total_Sales',
                     title=f'Top Bộ Phận Cửa Hàng {selected_store}',
                     labels={'Total_Sales': 'Tổng Doanh Số ($)', 'Dept': 'Bộ Phận'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Average sales by department
        fig = px.bar(top_depts, x='Dept', y='Avg_Sales',
                     title=f'Doanh Số Trung Bình Hàng Tuần Theo Bộ Phận - Cửa Hàng {selected_store}',
                     labels={'Avg_Sales': 'Doanh Số TB Hàng Tuần ($)', 'Dept': 'Bộ Phận'})
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()