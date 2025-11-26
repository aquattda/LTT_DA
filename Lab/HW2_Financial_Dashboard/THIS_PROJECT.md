# 📊 VN30 FINANCIAL DASHBOARD - TÀI LIỆU HOÀN CHỈNH

## 🎯 GIỚI THIỆU DỰ ÁN

### Mục tiêu
Xây dựng một Financial Dashboard hoàn chỉnh để phân tích và theo dõi 30 cổ phiếu hàng đầu của Việt Nam (VN-INDEX 30).

### Công nghệ sử dụng
- **Streamlit**: Framework web app cho Python
- **yfinance**: Lấy dữ liệu tài chính từ Yahoo Finance
- **Plotly**: Vẽ biểu đồ tương tác
- **Pandas & NumPy**: Xử lý và phân tích dữ liệu
- **Matplotlib**: Vẽ biểu đồ tĩnh

---

## 📁 CẤU TRÚC DỰ ÁN

```
HW2_Financial_Dashboard/
│
├── vn30_dashboard.py          # FILE CHÍNH - Dashboard Streamlit cho VN30
├── findash_demo.ipynb         # file demo qúa trình từng bước bởi các test
├── QUICK_START.md             # Tài liệu chi tiết đầy đủ
├── QUICK_START.md             # Hướng dẫn nhanh
├── THIS_PROJECT.md            # File này - Tổng quan dự án
│
└── requirements.txt           # Danh sách thư viện cần thiết
```

---

## 🌟 CÁC TÍNH NĂNG CHÍNH

### 1. 📊 Tổng Quan (Summary Tab)
**Mục đích**: Cung cấp cái nhìn tổng quan về cổ phiếu

**Tính năng**:
- Thông tin cơ bản: giá mở cửa, đóng cửa, bid/ask
- Khối lượng giao dịch
- Giá cao/thấp nhất trong ngày và 52 tuần
- Vốn hóa thị trường
- Biểu đồ giá lịch sử với range selector

**Công nghệ**:
```python
# Lấy thông tin từ yfinance
stock = yf.Ticker("VCB.VN")
info = stock.info

# Vẽ biểu đồ với Plotly
fig = px.area(data, x='Date', y='Close')
```

---

### 2. 📈 Biểu Đồ Kỹ Thuật (Chart Tab)
**Mục đích**: Phân tích kỹ thuật chuyên sâu

**Tính năng**:
- Chọn khoảng thời gian: Custom hoặc fixed (1M, 3M, 6M, YTD, 1Y, 3Y, 5Y, MAX)
- Chọn interval: 1 ngày, 1 tuần, 1 tháng
- Loại biểu đồ: Đường hoặc Nến (Candlestick)
- Hiển thị SMA 50 ngày
- Hiển thị khối lượng giao dịch (ở trục y phụ)

**Công nghệ**:
```python
# Biểu đồ với 2 trục y
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Nến
fig.add_trace(go.Candlestick(...), secondary_y=False)

# Volume
fig.add_trace(go.Bar(...), secondary_y=True)
```

---

### 3. 💰 Thông Tin Tài Chính (Financials Tab)
**Mục đích**: Xem báo cáo tài chính chi tiết

**Tính năng**:
- Báo cáo kết quả kinh doanh (Income Statement)
- Bảng cân đối kế toán (Balance Sheet)
- Báo cáo lưu chuyển tiền tệ (Cash Flow)
- Chu kỳ: Năm hoặc Quý

**Công nghệ**:
```python
stock = yf.Ticker("VCB.VN")

# Lấy báo cáo tài chính
income_stmt = stock.financials  # Năm
quarterly_income = stock.quarterly_financials  # Quý

balance_sheet = stock.balance_sheet
cash_flow = stock.cashflow
```

---

### 4. 🎲 Mô Phỏng Monte Carlo (Monte Carlo Tab)
**Mục đích**: Dự đoán xu hướng giá và đánh giá rủi ro

**Tính năng**:
- Chọn số lần mô phỏng: 200, 500, 1000
- Chọn thời gian dự đoán: 30, 60, 90 ngày
- Tính Value at Risk (VaR) với độ tin cậy 95%
- Biểu đồ phân phối giá dự đoán

**Công nghệ & Thuật toán**:
```python
# Bước 1: Tính volatility từ dữ liệu lịch sử
daily_return = close_price.pct_change()
daily_volatility = np.std(daily_return)

# Bước 2: Mô phỏng giá tương lai
for i in range(simulations):
    for day in range(time_horizon):
        future_return = np.random.normal(0, daily_volatility)
        future_price = last_price * (1 + future_return)
        
# Bước 3: Tính VaR
percentile_5 = np.percentile(ending_prices, 5)
VaR = current_price - percentile_5
```

**Giải thích VaR**: Value at Risk là ước tính thua lỗ tối đa có thể xảy ra với một mức độ tin cậy nhất định.

---

### 5. 📊 So Sánh Danh Mục (Portfolio Tab)
**Mục đích**: So sánh hiệu suất của nhiều cổ phiếu

**Tính năng**:
- Chọn nhiều cổ phiếu từ VN30
- Biểu đồ giá thực tế
- Biểu đồ chuẩn hóa (Base 100) để so sánh hiệu suất tương đối
- Thống kê: giá hiện tại, cao/thấp nhất, lợi nhuận TB, độ biến động, tổng thay đổi

**Công nghệ**:
```python
# Chuẩn hóa dữ liệu
df_normalized = (df / df.iloc[0]) * 100

# Tính thống kê
returns = df.pct_change()
volatility = returns.std()
total_return = (df.iloc[-1] - df.iloc[0]) / df.iloc[0]
```

---

### 6. ℹ️ Giới Thiệu VN30 (Info Tab)
**Mục đích**: Cung cấp thông tin về chỉ số VN30

**Tính năng**:
- Giải thích VN30 là gì
- Phân bổ theo ngành (Pie chart)
- Danh sách đầy đủ 30 cổ phiếu với tên đầy đủ
- Hướng dẫn sử dụng dashboard

---

## 🗂️ DANH SÁCH VN30 (30 CỔ PHIẾU)

### Ngân hàng (12)
```
VCB - Ngân hàng Ngoại thương Việt Nam
BID - Ngân hàng Đầu tư và Phát triển Việt Nam  
CTG - Ngân hàng Công thương Việt Nam
MBB - Ngân hàng Quân đội
TCB - Ngân hàng Kỹ thương Việt Nam
ACB - Ngân hàng Á Châu
HDB - Ngân hàng Phát triển TP.HCM
VPB - Ngân hàng Việt Nam Thịnh Vượng
TPB - Ngân hàng Tiên Phong
STB - Ngân hàng Sài Gòn Thương Tín
VIB - Ngân hàng Quốc tế Việt Nam
SSB - Ngân hàng Đông Nam Á
```

### Bất động sản (3)
```
VHM - Vinhomes
VIC - Vingroup
VRE - Vincom Retail
```

### Công nghiệp (3)
```
HPG - Hòa Phát
GVR - Cao su Việt Nam
BCM - Than - Khoáng sản Việt Nam
```

### Dầu khí & Năng lượng (3)
```
GAS - Khí Việt Nam
PLX - Xăng dầu Việt Nam
POW - Điện lực Dầu khí Việt Nam
```

### Tiêu dùng (4)
```
VNM - Vinamilk
SAB - Sabeco
MSN - Masan
MWG - Thế giới Di động
```

### Công nghệ (1)
```
FPT - FPT Corporation
```

### Chứng khoán (1)
```
SSI - Chứng khoán SSI
```

### Bảo hiểm (1)
```
BVH - Bảo Việt
```

### Hàng không (2)
```
VJC - Vietjet Air
HVN - Vietnam Airlines
```

---

## 🎨 THIẾT KẾ GIAO DIỆN

### Layout
```
┌─────────────────────────────────────────────────┐
│  Sidebar                │  Main Content Area    │
│  ┌──────────────────┐   │  ┌─────────────────┐  │
│  │ 🇻🇳 VN30         │   │  │  Tab Content    │  │
│  │ Dashboard        │   │  │                 │  │
│  │                  │   │  │  Charts         │  │
│  │ Select Ticker:   │   │  │  Tables         │  │
│  │ [Dropdown]       │   │  │  Metrics        │  │
│  │                  │   │  │                 │  │
│  │ Select Tab:      │   │  │                 │  │
│  │ ○ Tổng Quan     │   │  │                 │  │
│  │ ○ Biểu Đồ KT    │   │  │                 │  │
│  │ ○ Thông Tin TC  │   │  │                 │  │
│  │ ○ Monte Carlo   │   │  │                 │  │
│  │ ○ So Sánh DM    │   │  │                 │  │
│  │ ○ Giới Thiệu    │   │  │                 │  │
│  └──────────────────┘   │  └─────────────────┘  │
└─────────────────────────────────────────────────┘
```

### Màu sắc & Icons
- 📊 Biểu đồ: Blue tones
- 💰 Tài chính: Green tones  
- 🎲 Rủi ro: Red/Orange tones
- ℹ️ Info: Gray tones

---

## 🚀 HƯỚNG DẪN SỬ DỤNG

### Cài đặt
```bash
# 1. Cài đặt thư viện
pip install -r requirements.txt

# Hoặc cài đặt từng thư viện
pip install streamlit yfinance pandas numpy matplotlib plotly
```

### Chạy Dashboard
```bash
# Mở terminal tại thư mục dự án
cd "Lab/[HW2] Xay dung financial dashboard"

# Chạy
streamlit run vn30_dashboard.py

# Dashboard sẽ mở tại: http://localhost:8501
```

### Test trong Notebook
```bash
# Mở Jupyter Notebook
jupyter notebook

# Mở file: findash_demo.ipynb
# Chạy các cell theo thứ tự
```

## 📚 TÀI LIỆU THAM KHẢO

### Chính thức
1. [Streamlit Documentation](https://docs.streamlit.io/)
2. [yfinance GitHub](https://github.com/ranaroussi/yfinance)
3. [Plotly Python](https://plotly.com/python/)
4. [Pandas Documentation](https://pandas.pydata.org/docs/)

### Tutorial
1. [Streamlit Gallery](https://streamlit.io/gallery)
2. [Financial Analysis with Python](https://www.youtube.com/results?search_query=financial+analysis+python)
3. [Monte Carlo Simulation](https://www.investopedia.com/terms/m/montecarlosimulation.asp)


## 👤 THÔNG TIN TÁC GIẢ

**Sinh viên**: Luong Thanh Tuan  
**MSSV**: 3122410447  
**Lớp**: Data Analysis  
**Năm học**: 2024-2025

---

## 📝 GHI CHÚ

### Lưu ý khi sử dụng
- Dashboard chỉ mang tính tham khảo
- Không phải lời khuyên đầu tư
- Dữ liệu có thể bị trễ
- Cần Internet để hoạt động

### Credits
- Data source: Yahoo Finance
- Framework: Streamlit
- Inspiration: Financial analysis tools

---

**Chúc bạn sử dụng hiệu quả! 📊📈🚀**
