# 🎯 HƯỚNG DẪN SỬ DỤNG NOTEBOOK

## 📁 Files trong thư mục

1. **`sma_sorted.ipynb`** ✅ MỚI - KHUYẾN NGHỊ
   - Notebook đã sắp xếp theo thứ tự đúng
   - Có thêm thông tin chi tiết về mô hình Barabási-Albert
   - Chạy theo luồng từ trên xuống

2. **`sma.ipynb`** ⚠️ CŨ
   - Notebook gốc (thứ tự các cell bị ngược)
   - Không khuyến khích dùng

3. **`LUONG_CHAY.md`** 📖
   - Tài liệu chi tiết về luồng chạy
   - Giải thích từng bước
   - Kết quả mong đợi

## ⚡ CÁCH SỬ DỤNG NHANH

### Bước 1: Mở notebook mới
```
Mở file: sma_sorted.ipynb
```

### Bước 2: Chạy tất cả cells
```
Trong VS Code: Ctrl + Shift + P
→ Chọn "Notebook: Execute All Cells"

Hoặc: Click "Run All" ở thanh toolbar
```

### Bước 3: Xem kết quả
- Các biểu đồ sẽ hiển thị tự động
- File .gexf sẽ được tạo trong thư mục
- Dữ liệu sẽ lưu trong các biến

## 🔄 LUỒNG CHẠY NGẮN GỌN

```
1. Import thư viện
   ↓
2. Tạo mạng BA (300 nút, m=3)
   ↓
3. Phân tích tổng quan (đường kính, clustering, path length, phân phối bậc)
   ↓
4. Phân tích centrality (4 độ đo + PageRank + correlation)
   ↓
5. Phân tích cộng đồng (K-core + 4 thuật toán)
   ↓
6. Kết luận
```

## 📊 VỀ DỮ LIỆU BARABÁSI-ALBERT

### Tham số đã dùng:
```python
G = nx.barabasi_albert_graph(n=300, m=3, seed=42)
```

- **n=300**: 300 nút (người dùng)
- **m=3**: Mỗi nút mới kết nối 3 nút có sẵn
- **seed=42**: Để kết quả lặp lại được

### Đặc điểm:
- ✅ Scale-free network (tuân theo power-law)
- ✅ Có hub nodes (vài nút bậc rất cao)
- ✅ Small-world (đường đi ngắn)
- ✅ Clustering coefficient thấp

### Kết quả mong đợi:
- Tổng cạnh: ~894
- Bậc trung bình: ~6
- Đường kính: 6-7
- Gamma: 2.5-3.0
- R² power-law: >0.85

## 🚨 LỖI THƯỜNG GẶP

### Lỗi: `NameError: name 'nx' is not defined`
**Giải pháp**: Chạy cell import thư viện trước

### Lỗi: `NameError: name 'G' is not defined`
**Giải pháp**: Chạy cell tạo đồ thị trước

### Lỗi: Cell chạy quá lâu
**Giải pháp**: 
- Giảm n (số nút) xuống 200 hoặc 150
- Bỏ qua Girvan-Newman algorithm

## 📂 OUTPUT FILES

Sau khi chạy xong, bạn sẽ có:
- `network_for_gephi.gexf` - Đồ thị gốc
- `network_with_communities.gexf` - Đồ thị với thuộc tính cộng đồng

## 💡 MẸO

1. **Chạy lần đầu**: Dùng "Run All Cells"
2. **Sửa code**: Chạy lại từ cell đó trở đi
3. **Thay đổi dữ liệu**: Chỉ cần sửa cell tạo đồ thị, sau đó "Run All" lại
4. **Xuất Gephi**: Chạy đến cuối để có file .gexf hoàn chỉnh

## 📖 ĐỌC THÊM

- `LUONG_CHAY.md` - Tài liệu chi tiết từng bước
- `README.md` - Hướng dẫn cài đặt và tổng quan

---

**Tóm tắt**: Dùng `sma_sorted.ipynb` và chạy "Run All Cells" là xong! ✅
