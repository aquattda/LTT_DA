# Hướng Dẫn Nhanh - VN30 Financial Dashboard

## Bước 1: Cài đặt thư viện

Mở terminal/cmd và chạy:
```bash
pip install streamlit yfinance pandas numpy matplotlib plotly
```

## Bước 2: Chạy Dashboard

```bash
streamlit run vn30_dashboard.py
```

## Bước 3: Sử dụng
- Dashboard sẽ tự động mở trong trình duyệt
- Chọn mã cổ phiếu ở sidebar bên trái
- Chọn chức năng muốn xem

---

## Các chức năng chính

###  Tổng Quan

Xem thông tin cơ bản và biểu đồ giá

- Giá hiện tại, cao/thấp
- Khối lượng giao dịch
- Biểu đồ giá lịch sử

### Biểu Đồ Kỹ Thuật

Phân tích kỹ thuật chuyên sâu

- Biểu đồ nến (Candlestick)
- Đường SMA 50 ngày
- Khối lượng giao dịch

### Thông Tin Tài Chính

 Xem báo cáo tài chính

- Báo cáo kết quả kinh doanh
- Bảng cân đối kế toán
- Báo cáo lưu chuyển tiền tệ

### Mô Phỏng Monte Carlo

 Dự đoán giá và đánh giá rủi ro

- Chọn số lần mô phỏng (200/500/1000)
- Chọn thời gian dự đoán (30/60/90 ngày)
- Xem Value at Risk (VaR)

### So Sánh Danh Mục

 So sánh nhiều cổ phiếu cùng lúc

- Chọn nhiều mã cổ phiếu
- Xem biểu đồ so sánh
- Thống kê hiệu suất


## Hỗ trợ

Nếu gặp vấn đề:
1. Đọc kỹ file `THIS_PROJECT.md` để biết chi tiết
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
