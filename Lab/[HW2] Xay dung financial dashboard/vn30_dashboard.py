import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Danh sách 30 cổ phiếu VN30 
VN30_TICKERS = [
    'ACB.VN', 'BCM.VN', 'BID.VN', 'BVH.VN', 'CTG.VN', 
    'FPT.VN', 'GAS.VN', 'GVR.VN', 'HDB.VN', 'HPG.VN',
    'MBB.VN', 'MSN.VN', 'MWG.VN', 'PLX.VN', 'POW.VN',
    'SAB.VN', 'SSI.VN', 'STB.VN', 'TCB.VN', 'TPB.VN',
    'VCB.VN', 'VHM.VN', 'VIB.VN', 'VIC.VN', 'VJC.VN',
    'VNM.VN', 'VPB.VN', 'VRE.VN', 'SSB.VN', 'HVN.VN'
]

# Tên đầy đủ của các cổ phiếu
TICKER_NAMES = {
    'ACB.VN': 'ACB - Ngân hàng Á Châu',
    'BCM.VN': 'BCM - Tập đoàn Công nghiệp Than - Khoáng sản Việt Nam',
    'BID.VN': 'BID - Ngân hàng TMCP Đầu tư và Phát triển Việt Nam',
    'BVH.VN': 'BVH - Tập đoàn Bảo Việt',
    'CTG.VN': 'CTG - Ngân hàng TMCP Công thương Việt Nam',
    'FPT.VN': 'FPT - Tập đoàn FPT',
    'GAS.VN': 'GAS - Tổng Công ty Khí Việt Nam',
    'GVR.VN': 'GVR - Tập đoàn Công nghiệp Cao su Việt Nam',
    'HDB.VN': 'HDB - Ngân hàng TMCP Phát triển TP.HCM',
    'HPG.VN': 'HPG - Tập đoàn Hòa Phát',
    'MBB.VN': 'MBB - Ngân hàng TMCP Quân đội',
    'MSN.VN': 'MSN - Tập đoàn Masan',
    'MWG.VN': 'MWG - Thế giới Di động',
    'PLX.VN': 'PLX - Tập đoàn Xăng dầu Việt Nam',
    'POW.VN': 'POW - Tổng Công ty Điện lực Dầu khí Việt Nam',
    'SAB.VN': 'SAB - Tổng Công ty Cổ phần Bia - Rượu - Nước giải khát Sài Gòn',
    'SSI.VN': 'SSI - Chứng khoán SSI',
    'STB.VN': 'STB - Ngân hàng TMCP Sài Gòn Thương Tín',
    'TCB.VN': 'TCB - Ngân hàng TMCP Kỹ thương Việt Nam',
    'TPB.VN': 'TPB - Ngân hàng TMCP Tiên Phong',
    'VCB.VN': 'VCB - Ngân hàng TMCP Ngoại thương Việt Nam',
    'VHM.VN': 'VHM - Vinhomes',
    'VIB.VN': 'VIB - Ngân hàng TMCP Quốc tế Việt Nam',
    'VIC.VN': 'VIC - Tập đoàn Vingroup',
    'VJC.VN': 'VJC - Vietjet Air',
    'VNM.VN': 'VNM - Vinamilk',
    'VPB.VN': 'VPB - Ngân hàng TMCP Việt Nam Thịnh Vượng',
    'VRE.VN': 'VRE - Vincom Retail',
    'SSB.VN': 'SSB - Ngân hàng TMCP Đông Nam Á',
    'HVN.VN': 'HVN - Vietnam Airlines'
}

    
#==============================================================================
# Tab 1 - Tổng Quan (Summary)
#==============================================================================

def tab1():
    st.title("Tổng Quan Cổ Phiếu")
    
    if ticker == '-':
        st.info("Vui lòng chọn một mã cổ phiếu từ menu bên trái để bắt đầu")
        return
    
    st.subheader(f"{ticker.replace('.VN', '')} - {TICKER_NAMES.get(ticker, ticker)}")
    
    # Lấy thông tin cổ phiếu
    def getsummary(ticker):
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            table_info = {
                "Chỉ số": [],
                "Giá trị": [],
            }
            
            # Thông tin cơ bản
            metrics = [
                ("Giá đóng cửa trước", info.get("previousClose", "N/A")),
                ("Giá mở cửa", info.get("open", "N/A")),
                ("Giá bid", info.get("bid", "N/A")),
                ("Giá ask", info.get("ask", "N/A")),
                ("Khối lượng giao dịch", info.get("volume", "N/A")),
                ("Giá cao nhất trong ngày", info.get("dayHigh", "N/A")),
                ("Giá thấp nhất trong ngày", info.get("dayLow", "N/A")),
                ("Giá cao nhất 52 tuần", info.get("fiftyTwoWeekHigh", "N/A")),
                ("Giá thấp nhất 52 tuần", info.get("fiftyTwoWeekLow", "N/A")),
                ("Vốn hóa thị trường", info.get("marketCap", "N/A")),
            ]
            
            for name, value in metrics:
                table_info["Chỉ số"].append(name)
                if isinstance(value, (int, float)) and value != "N/A":
                    if name == "Vốn hóa thị trường":
                        table_info["Giá trị"].append(f"{value:,.0f} VNĐ")
                    elif name == "Khối lượng giao dịch":
                        table_info["Giá trị"].append(f"{value:,.0f}")
                    else:
                        table_info["Giá trị"].append(f"{value:,.0f} VNĐ")
                else:
                    table_info["Giá trị"].append(str(value))
            
            return pd.DataFrame(table_info)
        except Exception as e:
            st.error(f"Lỗi khi lấy thông tin: {str(e)}")
            return pd.DataFrame()
    
    # Hiển thị thông tin trong 2 cột
    c1, c2 = st.columns(2)
    
    with c1:
        summary = getsummary(ticker)
        if not summary.empty:
            st.dataframe(summary.iloc[:5], use_container_width=True, hide_index=True)
    
    with c2:
        summary = getsummary(ticker)
        if not summary.empty:
            st.dataframe(summary.iloc[5:], use_container_width=True, hide_index=True)
    
    # Vẽ biểu đồ giá lịch sử
    st.subheader("Biểu Đồ Giá Lịch Sử")
    
    @st.cache_data
    def getstockdata(ticker):
        try:
            stockdata = yf.download(ticker, period='max', progress=False)
            # Xử lý MultiIndex columns nếu có
            if isinstance(stockdata.columns, pd.MultiIndex):
                stockdata.columns = stockdata.columns.get_level_values(0)
            return stockdata
        except Exception as e:
            st.error(f"Lỗi khi tải dữ liệu: {str(e)}")
            return pd.DataFrame()
    
    chartdata = getstockdata(ticker)
    
    if not chartdata.empty:
        fig = px.area(chartdata, x=chartdata.index, y='Close', 
                     labels={'Close': 'Giá đóng cửa (VNĐ)', 'Date': 'Ngày'},
                     title=f'Biểu đồ giá {ticker.replace(".VN", "")}')
        
        fig.update_xaxes(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1 Tháng", step="month", stepmode="backward"),
                    dict(count=3, label="3 Tháng", step="month", stepmode="backward"),
                    dict(count=6, label="6 Tháng", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1 Năm", step="year", stepmode="backward"),
                    dict(count=3, label="3 Năm", step="year", stepmode="backward"),
                    dict(count=5, label="5 Năm", step="year", stepmode="backward"),
                    dict(label="Tất cả", step="all")
                ])
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Không có dữ liệu để hiển thị")


#==============================================================================
# Tab 2 - Biểu Đồ Kỹ Thuật (Chart)
#==============================================================================

def tab2():
    st.title("Biểu Đồ Kỹ Thuật")
    
    if ticker == '-':
        st.info("Vui lòng chọn một mã cổ phiếu từ menu bên trái")
        return
    
    st.subheader(f"{ticker.replace('.VN', '')} - {TICKER_NAMES.get(ticker, ticker)}")
    
    st.info("Đặt khoảng thời gian thành '-' để chọn khoảng ngày cụ thể")
    
    # Tùy chọn
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        start_date = st.date_input("Ngày bắt đầu", datetime.today().date() - timedelta(days=30))
    
    with c2:
        end_date = st.date_input("Ngày kết thúc", datetime.today().date())
    
    with c3:
        duration = st.selectbox("Khoảng thời gian", 
                               ['-', '1 Tháng', '3 Tháng', '6 Tháng', 'YTD', '1 Năm', '3 Năm', '5 Năm', 'Tất cả'])
        
        # Map tên tiếng Việt sang format Yahoo Finance
        duration_map = {
            '1 Tháng': '1mo',
            '3 Tháng': '3mo',
            '6 Tháng': '6mo',
            'YTD': 'ytd',
            '1 Năm': '1y',
            '3 Năm': '3y',
            '5 Năm': '5y',
            'Tất cả': 'max'
        }
        yf_duration = duration_map.get(duration, duration)
    
    with c4:
        inter = st.selectbox("Khoảng cách", ['1 ngày', '1 tuần', '1 tháng'])
        inter_map = {'1 ngày': '1d', '1 tuần': '1wk', '1 tháng': '1mo'}
        yf_interval = inter_map[inter]
    
    with c5:
        plot = st.selectbox("Loại biểu đồ", ['Đường', 'Nến'])
    
    # Lấy dữ liệu
    @st.cache_data
    def getchartdata(ticker, duration, start_date, end_date, interval):
        try:
            # Lấy dữ liệu cho SMA
            SMA_data = yf.download(ticker, period='max', progress=False)
            # Xử lý MultiIndex columns
            if isinstance(SMA_data.columns, pd.MultiIndex):
                SMA_data.columns = SMA_data.columns.get_level_values(0)
            
            if not SMA_data.empty:
                SMA_data['SMA'] = SMA_data['Close'].rolling(window=50).mean()
                SMA_data = SMA_data.reset_index()
                SMA_data = SMA_data[['Date', 'SMA']]
            
            # Lấy dữ liệu theo khoảng thời gian
            if duration != '-':
                chartdata = yf.download(ticker, period=duration, interval=interval, progress=False)
            else:
                chartdata = yf.download(ticker, start=start_date, end=end_date, interval=interval, progress=False)
            
            # Xử lý MultiIndex columns
            if isinstance(chartdata.columns, pd.MultiIndex):
                chartdata.columns = chartdata.columns.get_level_values(0)
            
            if not chartdata.empty:
                chartdata = chartdata.reset_index()
                if not SMA_data.empty:
                    chartdata = chartdata.merge(SMA_data, on='Date', how='left')
                return chartdata
            return pd.DataFrame()
        except Exception as e:
            st.error(f"Lỗi khi tải dữ liệu: {str(e)}")
            return pd.DataFrame()
    
    chartdata = getchartdata(ticker, yf_duration, start_date, end_date, yf_interval)
    
    if not chartdata.empty:
        # Tạo biểu đồ với 2 trục y
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # Vẽ biểu đồ giá
        if plot == 'Đường':
            fig.add_trace(
                go.Scatter(x=chartdata['Date'], y=chartdata['Close'], 
                          mode='lines', name='Giá đóng cửa', line=dict(color='blue')),
                secondary_y=False
            )
        else:
            fig.add_trace(
                go.Candlestick(
                    x=chartdata['Date'],
                    open=chartdata['Open'],
                    high=chartdata['High'],
                    low=chartdata['Low'],
                    close=chartdata['Close'],
                    name='Nến'
                ),
                secondary_y=False
            )
        
        # Vẽ đường SMA
        if 'SMA' in chartdata.columns:
            fig.add_trace(
                go.Scatter(x=chartdata['Date'], y=chartdata['SMA'], 
                          mode='lines', name='SMA 50 ngày', line=dict(color='orange')),
                secondary_y=False
            )
        
        # Vẽ khối lượng giao dịch
        fig.add_trace(
            go.Bar(x=chartdata['Date'], y=chartdata['Volume'], 
                  name='Khối lượng', marker=dict(color='lightblue')),
            secondary_y=True
        )
        
        # Cập nhật layout
        fig.update_yaxes(range=[0, chartdata['Volume'].max() * 3], 
                        showticklabels=False, secondary_y=True)
        fig.update_yaxes(title_text="Giá (VNĐ)", secondary_y=False)
        fig.update_xaxes(title_text="Ngày")
        
        fig.update_layout(
            title=f'Biểu đồ kỹ thuật {ticker.replace(".VN", "")}',
            height=600,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Không có dữ liệu để hiển thị")


#==============================================================================
# Tab 3 - Thông Tin Tài Chính (Financials)
#==============================================================================

def tab3():
    st.title("Thông Tin Tài Chính")
    
    if ticker == '-':
        st.info("Vui lòng chọn một mã cổ phiếu từ menu bên trái")
        return
    
    st.subheader(f"{ticker.replace('.VN', '')} - {TICKER_NAMES.get(ticker, ticker)}")
    
    statement = st.selectbox("Loại báo cáo", ['Báo cáo kết quả kinh doanh', 'Bảng cân đối kế toán', 'Báo cáo lưu chuyển tiền tệ'])
    period = st.selectbox("Chu kỳ", ['Năm', 'Quý'])
    
    @st.cache_data
    def get_financial_data(ticker, statement_type, yearly=True):
        try:
            stock = yf.Ticker(ticker)
            
            if statement_type == 'Báo cáo kết quả kinh doanh':
                data = stock.financials if yearly else stock.quarterly_financials
            elif statement_type == 'Bảng cân đối kế toán':
                data = stock.balance_sheet if yearly else stock.quarterly_balance_sheet
            else:  # Báo cáo lưu chuyển tiền tệ
                data = stock.cashflow if yearly else stock.quarterly_cashflow
            
            if not data.empty:
                # Chuyển đổi số liệu sang VNĐ (ước lượng)
                data = data / 1000  # Chuyển sang nghìn
                return data
            return pd.DataFrame()
        except Exception as e:
            st.error(f"Lỗi khi tải dữ liệu: {str(e)}")
            return pd.DataFrame()
    
    yearly = (period == 'Năm')
    data = get_financial_data(ticker, statement, yearly)
    
    if not data.empty:
        st.dataframe(data, use_container_width=True)
        
        # Hiển thị chú thích
        st.caption("Đơn vị: Nghìn VNĐ")
    else:
        st.warning("Không có dữ liệu tài chính cho cổ phiếu này")


#==============================================================================
# Tab 4 - Mô Phỏng Monte Carlo
#==============================================================================

def tab4():
    st.title("Mô Phỏng Monte Carlo")
    
    if ticker == '-':
        st.info("Vui lòng chọn một mã cổ phiếu từ menu bên trái")
        return
    
    st.subheader(f"{ticker.replace('.VN', '')} - {TICKER_NAMES.get(ticker, ticker)}")
    
    st.info("Mô phỏng Monte Carlo giúp dự đoán xu hướng giá cổ phiếu trong tương lai dựa trên dữ liệu lịch sử")
    
    # Tùy chọn
    c1, c2 = st.columns(2)
    with c1:
        simulations = st.selectbox("Số lần mô phỏng (n)", [200, 500, 1000])
    with c2:
        time_horizon = st.selectbox("Thời gian dự đoán (ngày)", [30, 60, 90])
    
    @st.cache_data
    def montecarlo(ticker, time_horizon, simulations):
        try:
            # Lấy dữ liệu 30 ngày gần nhất
            end_date = datetime.now()
            start_date = end_date - timedelta(days=60)
            
            stock_price = yf.download(ticker, start=start_date, end=end_date, progress=False)
            
            # Xử lý MultiIndex columns
            if isinstance(stock_price.columns, pd.MultiIndex):
                stock_price.columns = stock_price.columns.get_level_values(0)
            
            if stock_price.empty:
                return pd.DataFrame(), None
            
            close_price = stock_price['Close']
            
            # Tính toán lợi nhuận hàng ngày và độ biến động
            daily_return = close_price.pct_change()
            daily_volatility = np.std(daily_return)
            
            # Khởi tạo dataframe cho mô phỏng
            simulation_df = pd.DataFrame()
            
            for i in range(simulations):
                next_price = []
                last_price = close_price.iloc[-1]
                
                for x in range(time_horizon):
                    future_return = np.random.normal(0, daily_volatility)
                    future_price = last_price * (1 + future_return)
                    next_price.append(future_price)
                    last_price = future_price
                
                simulation_df[i] = next_price
            
            return simulation_df, close_price.iloc[-1]
        except Exception as e:
            st.error(f"Lỗi khi mô phỏng: {str(e)}")
            return pd.DataFrame(), None
    
    if st.button("Chạy Mô Phỏng", type="primary"):
        with st.spinner("Đang thực hiện mô phỏng..."):
            mc, current_price = montecarlo(ticker, time_horizon, simulations)
            
            if not mc.empty and current_price is not None:
                # Vẽ biểu đồ mô phỏng
                fig, ax = plt.subplots(figsize=(15, 8))
                ax.plot(mc, alpha=0.3)
                plt.title(f'Mô phỏng Monte Carlo cho {ticker.replace(".VN", "")} - {time_horizon} ngày tiếp theo', 
                         fontsize=16, fontweight='bold')
                plt.xlabel('Ngày', fontsize=12)
                plt.ylabel('Giá (VNĐ)', fontsize=12)
                plt.axhline(y=current_price, color='red', linestyle='--', linewidth=2)
                plt.legend([f'Giá hiện tại: {current_price:,.0f} VNĐ'], fontsize=12)
                plt.grid(True, alpha=0.3)
                st.pyplot(fig)
                
                # Phân tích Value at Risk (VaR)
                st.subheader('Phân Tích Rủi Ro - Value at Risk (VaR)')
                
                ending_price = mc.iloc[-1, :].values
                
                fig1, ax = plt.subplots(figsize=(15, 6))
                ax.hist(ending_price, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
                percentile_5 = np.percentile(ending_price, 5)
                plt.axvline(percentile_5, color='red', linestyle='--', linewidth=2)
                plt.legend([f'Giá ở phân vị 5%: {percentile_5:,.0f} VNĐ'], fontsize=12)
                plt.title(f'Phân phối giá sau {time_horizon} ngày', fontsize=16, fontweight='bold')
                plt.xlabel('Giá (VNĐ)', fontsize=12)
                plt.ylabel('Tần suất', fontsize=12)
                plt.grid(True, alpha=0.3)
                st.pyplot(fig1)
                
                # Tính toán VaR
                VaR = current_price - percentile_5
                
                # Hiển thị kết quả
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Giá hiện tại", f"{current_price:,.0f} VNĐ")
                with col2:
                    st.metric("Giá dự đoán (5% thấp nhất)", f"{percentile_5:,.0f} VNĐ")
                with col3:
                    st.metric("VaR (95% tin cậy)", f"{VaR:,.0f} VNĐ", 
                             delta=f"{(VaR/current_price*100):.2f}%", delta_color="inverse")
                
                st.info(f"**Giải thích**: Với độ tin cậy 95%, rủi ro tối đa trong {time_horizon} ngày tới là {VaR:,.0f} VNĐ ({(VaR/current_price*100):.2f}% giá hiện tại)")
            else:
                st.error("Không thể thực hiện mô phỏng. Vui lòng thử lại.")


#==============================================================================
# Tab 5 - So Sánh Danh Mục
#==============================================================================

def tab5():
    st.title("So Sánh Danh Mục Đầu Tư")
    
    st.info("Chọn nhiều cổ phiếu để so sánh xu hướng giá")
    
    selected_tickers = st.multiselect(
        "Chọn các mã cổ phiếu trong danh mục của bạn",
        options=VN30_TICKERS,
        default=['VCB.VN', 'VIC.VN', 'HPG.VN'],
        format_func=lambda x: f"{x.replace('.VN', '')} - {TICKER_NAMES.get(x, x)}"
    )
    
    if not selected_tickers:
        st.warning("Vui lòng chọn ít nhất một cổ phiếu")
        return
    
    # Tùy chọn khoảng thời gian
    period = st.selectbox("Khoảng thời gian", 
                         ['1 Tháng', '3 Tháng', '6 Tháng', '1 Năm', '3 Năm', '5 Năm'],
                         index=3)
    
    period_map = {
        '1 Tháng': '1mo',
        '3 Tháng': '3mo',
        '6 Tháng': '6mo',
        '1 Năm': '1y',
        '3 Năm': '3y',
        '5 Năm': '5y'
    }
    
    @st.cache_data
    def get_portfolio_data(tickers, period):
        df = pd.DataFrame()
        for ticker in tickers:
            try:
                data = yf.download(ticker, period=period, progress=False)
                # Xử lý MultiIndex columns
                if isinstance(data.columns, pd.MultiIndex):
                    data.columns = data.columns.get_level_values(0)
                
                if not data.empty:
                    df[ticker.replace('.VN', '')] = data['Close']
            except Exception as e:
                st.warning(f"Không thể tải dữ liệu cho {ticker}: {str(e)}")
        return df
    
    df = get_portfolio_data(selected_tickers, period_map[period])
    
    if not df.empty:
        # Chuẩn hóa dữ liệu (base 100)
        df_normalized = (df / df.iloc[0]) * 100
        
        # Tab cho biểu đồ gốc và chuẩn hóa
        tab_raw, tab_normalized = st.tabs(["Giá Thực Tế", "So Sánh Chuẩn Hóa (Base 100)"])
        
        with tab_raw:
            fig1 = px.line(df, title=f'Xu hướng giá các cổ phiếu - {period}')
            fig1.update_layout(
                xaxis_title="Ngày",
                yaxis_title="Giá (VNĐ)",
                hovermode='x unified',
                height=500
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with tab_normalized:
            fig2 = px.line(df_normalized, title=f'So sánh hiệu suất (Base 100) - {period}')
            fig2.update_layout(
                xaxis_title="Ngày",
                yaxis_title="Chỉ số (Base 100)",
                hovermode='x unified',
                height=500
            )
            st.plotly_chart(fig2, use_container_width=True)
            
            st.info("**Chú thích**: Biểu đồ chuẩn hóa giúp so sánh hiệu suất tương đối giữa các cổ phiếu, bất kể mức giá ban đầu")
        
        # Thống kê
        st.subheader("Thống Kê Danh Mục")
        
        returns = df.pct_change().dropna()
        
        stats = pd.DataFrame({
            'Giá hiện tại (VNĐ)': df.iloc[-1],
            'Giá cao nhất (VNĐ)': df.max(),
            'Giá thấp nhất (VNĐ)': df.min(),
            'Lợi nhuận TB hàng ngày (%)': returns.mean() * 100,
            'Độ biến động (%)': returns.std() * 100,
            'Tổng thay đổi (%)': ((df.iloc[-1] - df.iloc[0]) / df.iloc[0] * 100)
        })
        
        st.dataframe(stats.T, use_container_width=True)
    else:
        st.error("Không thể tải dữ liệu cho các cổ phiếu đã chọn")


#==============================================================================
# Tab 6 - Thông Tin VN30
#==============================================================================

def tab6():
    st.title("Giới Thiệu VN30")
    
    st.markdown("""
    ### VN30 là gì?
    
    **VN30** (Vietnam National Stock Exchange - Top 30) là chỉ số gồm 30 cổ phiếu có vốn hóa lớn nhất và 
    thanh khoản cao nhất trên Sở Giao dịch Chứng khoán TP. Hồ Chí Minh (HOSE).
    
    ### Đặc điểm:
    - 30 cổ phiếu blue-chip hàng đầu
    - Được review và điều chỉnh định kỳ
    - Đại diện cho các ngành then chốt của nền kinh tế
    - Thanh khoản cao, phù hợp cho đầu tư dài hạn
    
    ### Phân bổ theo ngành:
    """)
    
    # Phân loại theo ngành
    sectors = {
        'Ngân hàng': ['VCB.VN', 'BID.VN', 'CTG.VN', 'MBB.VN', 'TCB.VN', 'ACB.VN', 'HDB.VN', 'VPB.VN', 'TPB.VN', 'STB.VN', 'VIB.VN', 'SSB.VN'],
        'Bất động sản': ['VHM.VN', 'VIC.VN', 'VRE.VN'],
        'Công nghiệp': ['HPG.VN', 'GVR.VN', 'BCM.VN'],
        'Dầu khí & Năng lượng': ['GAS.VN', 'PLX.VN', 'POW.VN'],
        'Tiêu dùng': ['VNM.VN', 'SAB.VN', 'MSN.VN', 'MWG.VN'],
        'Công nghệ': ['FPT.VN'],
        'Chứng khoán': ['SSI.VN'],
        'Bảo hiểm': ['BVH.VN'],
        'Hàng không': ['VJC.VN', 'HVN.VN']
    }
    
    sector_count = {sector: len(tickers) for sector, tickers in sectors.items()}
    
    fig = px.pie(
        values=list(sector_count.values()),
        names=list(sector_count.keys()),
        title='Phân bổ cổ phiếu VN30 theo ngành'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Danh sách chi tiết
    st.subheader("Danh Sách Đầy Đủ 30 Cổ Phiếu VN30")
    
    vn30_info = []
    for ticker in VN30_TICKERS:
        code = ticker.replace('.VN', '')
        name = TICKER_NAMES.get(ticker, ticker)
        # Tìm ngành
        sector = next((s for s, t in sectors.items() if ticker in t), 'Khác')
        vn30_info.append({'Mã CK': code, 'Tên công ty': name, 'Ngành': sector})
    
    df_info = pd.DataFrame(vn30_info)
    st.dataframe(df_info, use_container_width=True, hide_index=True)
    
    st.markdown("""
    ---
    ### Cách sử dụng Dashboard:
    
    1. **Tổng Quan**: Xem thông tin cơ bản và biểu đồ giá lịch sử
    2. **Biểu Đồ Kỹ Thuật**: Phân tích kỹ thuật với các công cụ như SMA, biểu đồ nến
    3. **Thông Tin Tài Chính**: Xem các báo cáo tài chính chi tiết
    4. **Mô Phỏng Monte Carlo**: Dự đoán xu hướng giá và đánh giá rủi ro
    5. **So Sánh Danh Mục**: So sánh hiệu suất của nhiều cổ phiếu
    
    ---
    **Lưu ý**: Dữ liệu được cung cấp bởi Yahoo Finance. Dashboard này chỉ mang tính chất tham khảo, 
    không phải lời khuyên đầu tư.
    """)


#==============================================================================
# Main body
#==============================================================================

def run():
    # Cấu hình trang
    st.set_page_config(
        page_title="VN30 Financial Dashboard",
        page_icon="🇻🇳",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # CSS tùy chỉnh
    st.markdown("""
        <style>
        .main {
            padding: 0rem 1rem;
        }
        .stSelectbox {
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("🇻🇳 VN30 Financial Dashboard")
    st.sidebar.markdown("---")
    
    # Chọn cổ phiếu
    ticker_list = ['-'] + VN30_TICKERS
    
    global ticker
    ticker = st.sidebar.selectbox(
        "Chọn mã cổ phiếu",
        ticker_list,
        format_func=lambda x: f"{x.replace('.VN', '')} - {TICKER_NAMES.get(x, 'Chọn cổ phiếu')}" if x != '-' else '-- Chọn cổ phiếu --'
    )
    
    st.sidebar.markdown("---")
    
    # Chọn tab
    select_tab = st.sidebar.radio(
        "Chọn chức năng",
        ['Tổng Quan', 'Biểu Đồ Kỹ Thuật', 'Thông Tin Tài Chính', 
         'Mô Phỏng Monte Carlo', 'So Sánh Danh Mục', 'Giới Thiệu VN30']
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Dashboard VN30**
    
    Công cụ phân tích và theo dõi 
    30 cổ phiếu hàng đầu Việt Nam
    
    Dữ liệu: Yahoo Finance
    """)
    
    # Hiển thị tab được chọn
    if select_tab == 'Tổng Quan':
        tab1()
    elif select_tab == 'Biểu Đồ Kỹ Thuật':
        tab2()
    elif select_tab == 'Thông Tin Tài Chính':
        tab3()
    elif select_tab == 'Mô Phỏng Monte Carlo':
        tab4()
    elif select_tab == 'So Sánh Danh Mục':
        tab5()
    elif select_tab == 'Giới Thiệu VN30':
        tab6()


if __name__ == "__main__":
    run()
