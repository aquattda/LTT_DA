# 🐛 Bug Fix: MultiIndex Columns Issue

## ❌ Lỗi gặp phải

```
ValueError: Value of 'y' is not the name of a column in 'data_frame'. 
Expected one of [('Close', 'BID.VN'), ('High', 'BID.VN'), ('Low', 'BID.VN'), 
('Open', 'BID.VN'), ('Volume', 'BID.VN')] but received: Close
```

## 🔍 Nguyên nhân

Khi sử dụng `yfinance` để download dữ liệu cổ phiếu, đôi khi API trả về DataFrame với **MultiIndex columns** thay vì single-level columns.

### Cấu trúc bình thường:
```
Columns: ['Open', 'High', 'Low', 'Close', 'Volume']
```

### Cấu trúc MultiIndex (gây lỗi):
```
Columns: [('Open', 'BID.VN'), ('High', 'BID.VN'), ('Low', 'BID.VN'), 
          ('Close', 'BID.VN'), ('Volume', 'BID.VN')]
```

Khi cố gắng truy cập `data['Close']` với MultiIndex columns, Python không tìm thấy cột 'Close' đơn giản, mà chỉ tìm thấy tuple `('Close', 'BID.VN')`.

## ✅ Giải pháp

Thêm đoạn code kiểm tra và flatten MultiIndex columns sau mỗi lần download dữ liệu:

```python
import pandas as pd
import yfinance as yf

# Download dữ liệu
data = yf.download('VCB.VN', period='1y', progress=False)

# Kiểm tra và xử lý MultiIndex columns
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Bây giờ có thể truy cập bình thường
close_price = data['Close']  # ✅ Hoạt động
```

## 📝 Các file đã sửa

### 1. vn30_dashboard.py

#### Tab 1 - Function `getstockdata`
```python
@st.cache_data
def getstockdata(ticker):
    try:
        stockdata = yf.download(ticker, period='max', progress=False)
        # ✅ Thêm xử lý MultiIndex
        if isinstance(stockdata.columns, pd.MultiIndex):
            stockdata.columns = stockdata.columns.get_level_values(0)
        return stockdata
    except Exception as e:
        st.error(f"Lỗi khi tải dữ liệu: {str(e)}")
        return pd.DataFrame()
```

#### Tab 2 - Function `getchartdata`
```python
@st.cache_data
def getchartdata(ticker, duration, start_date, end_date, interval):
    try:
        # Lấy dữ liệu cho SMA
        SMA_data = yf.download(ticker, period='max', progress=False)
        # ✅ Xử lý MultiIndex
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
        
        # ✅ Xử lý MultiIndex
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
```

#### Tab 4 - Function `montecarlo`
```python
@st.cache_data
def montecarlo(ticker, time_horizon, simulations):
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=60)
        
        stock_price = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        # ✅ Xử lý MultiIndex
        if isinstance(stock_price.columns, pd.MultiIndex):
            stock_price.columns = stock_price.columns.get_level_values(0)
        
        if stock_price.empty:
            return pd.DataFrame(), None
        
        close_price = stock_price['Close']
        # ... rest of the code
```

#### Tab 5 - Function `get_portfolio_data`
```python
@st.cache_data
def get_portfolio_data(tickers, period):
    df = pd.DataFrame()
    for ticker in tickers:
        try:
            data = yf.download(ticker, period=period, progress=False)
            # ✅ Xử lý MultiIndex
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)
            
            if not data.empty:
                df[ticker.replace('.VN', '')] = data['Close']
        except Exception as e:
            st.warning(f"Không thể tải dữ liệu cho {ticker}: {str(e)}")
    return df
```

### 2. findash_demo.ipynb

Đã cập nhật tất cả các function tương tự trong notebook demo:
- Cell `getstockdata()`
- Cell biểu đồ Candlestick
- Cell `montecarlo()`
- Cell so sánh nhiều cổ phiếu

## 🎯 Khi nào cần dùng

### ✅ Luôn luôn kiểm tra sau khi download
```python
data = yf.download(ticker, ...)

# Bắt buộc kiểm tra
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)
```

### ⚠️ Đặc biệt quan trọng khi:
1. Download một ticker duy nhất
2. Sử dụng với Plotly (px.line, px.area, etc.)
3. Truy cập cột trực tiếp (`data['Close']`)
4. Tính toán với các cột (`data['Close'].rolling()`)

## 🧪 Cách test

```python
import yfinance as yf
import pandas as pd

# Test 1: Kiểm tra cấu trúc columns
ticker = "VCB.VN"
data = yf.download(ticker, period="1mo", progress=False)

print("Type of columns:", type(data.columns))
print("Columns:", data.columns.tolist())

if isinstance(data.columns, pd.MultiIndex):
    print("⚠️ MultiIndex detected!")
    data.columns = data.columns.get_level_values(0)
    print("✅ Fixed!")
    print("New columns:", data.columns.tolist())

# Test 2: Thử truy cập
try:
    close = data['Close']
    print("✅ Successfully accessed 'Close' column")
except KeyError as e:
    print(f"❌ Error: {e}")
```

## 📊 Kết quả

Sau khi áp dụng fix:
- ✅ Tất cả các tab đều hoạt động bình thường
- ✅ Biểu đồ hiển thị chính xác
- ✅ Không còn lỗi ValueError
- ✅ Code robust hơn, xử lý cả 2 trường hợp

## 🔗 Tham khảo

- [pandas MultiIndex Documentation](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html)
- [yfinance GitHub Issues](https://github.com/ranaroussi/yfinance/issues)
- [Stack Overflow: MultiIndex columns in yfinance](https://stackoverflow.com/questions/tagged/yfinance+multiindex)

## 💡 Best Practice

Tạo một helper function để tái sử dụng:

```python
def download_and_clean(ticker, **kwargs):
    """
    Download stock data and clean MultiIndex columns if present
    
    Args:
        ticker: Stock ticker symbol
        **kwargs: Additional arguments for yf.download()
    
    Returns:
        pd.DataFrame: Clean dataframe with single-level columns
    """
    data = yf.download(ticker, **kwargs)
    
    # Clean MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    
    return data

# Sử dụng
data = download_and_clean('VCB.VN', period='1y', progress=False)
```

---

**Ngày cập nhật**: 13/11/2025  
**Trạng thái**: ✅ Đã sửa hoàn toàn  
**Tested**: ✅ Tất cả functions đã test
