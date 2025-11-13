# 🚀 Hướng Dẫn Nhanh - VN30 Financial Dashboard

## ⚡ Bắt đầu ngay (3 bước)

### Bước 1: Cài đặt thư viện
Mở terminal/cmd và chạy:
```bash
pip install streamlit yfinance pandas numpy matplotlib plotly
```

### Bước 2: Chạy Dashboard
```bash
streamlit run vn30_dashboard.py
```

### Bước 3: Sử dụng
- Dashboard sẽ tự động mở trong trình duyệt
- Chọn mã cổ phiếu ở sidebar bên trái
- Chọn chức năng muốn xem

---

## 🎯 Các chức năng chính

### 📊 Tổng Quan
👉 Xem thông tin cơ bản và biểu đồ giá
- Giá hiện tại, cao/thấp
- Khối lượng giao dịch
- Biểu đồ giá lịch sử

### 📈 Biểu Đồ Kỹ Thuật
👉 Phân tích kỹ thuật chuyên sâu
- Biểu đồ nến (Candlestick)
- Đường SMA 50 ngày
- Khối lượng giao dịch

### 💰 Thông Tin Tài Chính
👉 Xem báo cáo tài chính
- Báo cáo kết quả kinh doanh
- Bảng cân đối kế toán
- Báo cáo lưu chuyển tiền tệ

### 🎲 Mô Phỏng Monte Carlo
👉 Dự đoán giá và đánh giá rủi ro
- Chọn số lần mô phỏng (200/500/1000)
- Chọn thời gian dự đoán (30/60/90 ngày)
- Xem Value at Risk (VaR)

### 📊 So Sánh Danh Mục
👉 So sánh nhiều cổ phiếu cùng lúc
- Chọn nhiều mã cổ phiếu
- Xem biểu đồ so sánh
- Thống kê hiệu suất

---

## 💡 Ví dụ nhanh

### Test trong Jupyter Notebook

```python
import yfinance as yf

# Lấy dữ liệu VCB
ticker = "VCB.VN"
data = yf.download(ticker, period="1mo")
print(data.tail())

# Lấy thông tin cơ bản
stock = yf.Ticker(ticker)
print(stock.info)
```

### Chạy Dashboard

```bash
# Đảm bảo bạn đang ở đúng thư mục
cd "Lab/[HW2] Xay dung financial dashboard"

# Chạy
streamlit run vn30_dashboard.py
```

---

## 🔍 Danh sách cổ phiếu VN30

### Top 5 cổ phiếu phổ biến:
1. **VCB** - Vietcombank
2. **VIC** - Vingroup  
3. **HPG** - Hòa Phát
4. **FPT** - FPT Corporation
5. **MWG** - Thế giới Di động

### Các ngành chính:
- 🏦 **Ngân hàng**: VCB, BID, CTG, MBB, TCB...
- 🏢 **Bất động sản**: VHM, VIC, VRE
- ⚙️ **Công nghiệp**: HPG, GVR, BCM
- ⛽ **Dầu khí**: GAS, PLX, POW
- 🛒 **Tiêu dùng**: VNM, MWG, MSN
- 💻 **Công nghệ**: FPT

---

## ⚠️ Lưu ý quan trọng

### ✅ Nên:
- Có kết nối Internet khi sử dụng
- Chọn khoảng thời gian phù hợp để tránh quá tải dữ liệu
- Sử dụng để tham khảo và học tập

### ❌ Không nên:
- Coi đây là lời khuyên đầu tư
- Sử dụng cho giao dịch thực tế mà không có kiến thức đầy đủ
- Tin tưởng hoàn toàn vào mô phỏng Monte Carlo

---

## 🐛 Xử lý lỗi thường gặp

### Lỗi 1: Import Error
```bash
# Giải quyết: Cài đặt lại thư viện
pip install --upgrade streamlit yfinance plotly
```

### Lỗi 2: Không tải được dữ liệu
```python
# Kiểm tra format mã cổ phiếu
ticker = "VCB.VN"  # ✅ Đúng
ticker = "VCB"      # ❌ Sai (thiếu .VN)
```

### Lỗi 3: Dashboard không mở
```bash
# Thử chạy với port khác
streamlit run vn30_dashboard.py --server.port 8502
```

---

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Đọc kỹ file `README_VN30.md` để biết chi tiết
2. Kiểm tra file `findash_demo.ipynb` để test từng chức năng
3. Đảm bảo đã cài đặt đủ thư viện trong `requirements.txt`

---

## 🎓 Học thêm

### Tài nguyên hữu ích:
- [Streamlit Tutorial](https://docs.streamlit.io/get-started)
- [yfinance Examples](https://github.com/ranaroussi/yfinance/wiki/Usage-examples)
- [Plotly Tutorial](https://plotly.com/python/getting-started/)

---

**Chúc bạn thành công! 🚀📊**
