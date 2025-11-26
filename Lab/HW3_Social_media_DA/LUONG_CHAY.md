# 📊 LUỒNG CHẠY PHÂN TÍCH MẠNG XÃ HỘI

## 🎯 MỤC ĐÍCH
Hướng dẫn chi tiết luồng chạy từng bước để phân tích mạng xã hội một cách có hệ thống.

---

## 📁 NGUỒN DỮ LIỆU MẪU: BARABASI-ALBERT

### 🔍 Giới thiệu
**Mô hình Barabási-Albert (BA)** là mô hình sinh mạng scale-free, mô phỏng cách các mạng thực tế phát triển.

### 📊 Đặc điểm mạng BA
- **Cơ chế**: Preferential attachment (nút mới ưu tiên kết nối với nút có bậc cao)
- **Phân phối bậc**: Tuân theo power-law P(k) ~ k^(-γ)
- **Ứng dụng**: Mô phỏng mạng xã hội, Internet, mạng trích dẫn

### 🔧 Tham số trong code
```python
G = nx.barabasi_albert_graph(n=300, m=3, seed=42)
```

**Giải thích tham số:**
- `n=300`: Số nút trong mạng (300 người dùng)
- `m=3`: Mỗi nút mới kết nối với 3 nút hiện có
- `seed=42`: Seed cho random (để kết quả lặp lại được)

### 📈 Kết quả mong đợi
- Tổng số nút: 300
- Tổng số cạnh: ≈ 894 (vì mỗi nút mới thêm 3 cạnh, trừ m nút đầu tiên)
- Phân phối bậc: Power-law với γ ≈ 2.9 - 3.0
- Có các hub nodes (bậc rất cao)
- Hệ số phân cụm thấp
- Độ dài đường đi trung bình nhỏ (small-world)

---

## 🔄 LUỒNG 1: CHUẨN BỊ DỮ LIỆU

### **Bước 1.1: Khởi tạo Notebook**
```
✅ Cell: Tiêu đề và mục lục (Markdown)
✅ Cell: Phần 1 - Tổng quan đề tài (Markdown)
```
**Output**: Cấu trúc báo cáo

---

### **Bước 1.2: Import thư viện**
```
✅ Cell: Import libraries
   - networkx, pandas, numpy
   - matplotlib, seaborn
   - scipy, collections
```
**Output**: "Các thư viện đã được import thành công!"

**Kiểm tra**: Không có lỗi import

---

### **Bước 1.3: Load dữ liệu mạng**
```
✅ Cell: Markdown - Hướng dẫn chọn nguồn dữ liệu
✅ Cell: Tạo mạng BA (Cách 1)
   G = nx.barabasi_albert_graph(n=300, m=3, seed=42)
✅ Cell: Markdown - Hướng dẫn load từ file
✅ Cell: Code load từ file (commented)
```
**Output**: 
```
Đồ thị đã được tạo: Graph with 300 nodes and 894 edges
```

**Kiểm tra**: 
- `G` là đối tượng Graph
- `print(nx.info(G))` hiển thị thông tin đúng

---

## 🔍 LUỒNG 2: PHÂN TÍCH TỔNG QUAN MẠNG

### **Bước 2.1: Kiểm tra kiểu đồ thị**
```
✅ Cell: Xác định kiểu đồ thị
   - Có hướng/vô hướng
   - Có trọng số/không
   - Tính liên thông
   - Tạo G_lcc (largest connected component)
```
**Output**: 
```
THÔNG TIN CƠ BẢN VỀ MẠNG
- Kiểu đồ thị: Graph (vô hướng, không trọng số)
- Số nút: 300
- Số cạnh: 894
- Mật độ: 0.019933
- Liên thông: True
```

**Biến quan trọng**: `G_lcc` (dùng cho các tính toán sau)

---

### **Bước 2.2: Đường kính và bán kính**
```
✅ Cell: Tính diameter, radius, center, periphery
```
**Output**: 
```
- Đường kính: ~6-7
- Bán kính: ~4
- Center nodes: [...]
- Periphery nodes: [...]
```

---

### **Bước 2.3: Hệ số phân cụm**
```
✅ Cell: Tính clustering coefficient
   - Global clustering
   - Average clustering
   - Histogram phân phối
```
**Output**:
```
- Hệ số phân cụm toàn cục: ~0.02-0.05
- Hệ số phân cụm trung bình: ~0.03-0.06
+ Biểu đồ histogram
```

---

### **Bước 2.4: Độ dài đường đi trung bình**
```
✅ Cell: Tính average shortest path length
   - Histogram phân phối độ dài
```
**Output**:
```
- Độ dài đường đi trung bình: ~3.5-4.5
+ Biểu đồ phân phối
```

**Nhận xét**: Mạng có tính chất small-world

---

### **Bước 2.5: Phân phối bậc**
```
✅ Cell: Phân tích degree distribution
   - Histogram (linear scale)
   - Log-log plot
   - Thống kê: mean, median, std
```
**Output**:
```
- Bậc trung bình: ~6
- Bậc max: ~30-50
+ 2 biểu đồ (linear & log-log)
```

---

### **Bước 2.6: Hồi quy Power-law**
```
✅ Cell: Power-law regression
   - Tính gamma
   - Tính R²
   - Vẽ đường hồi quy
```
**Output**:
```
- Gamma (γ): ~2.5-3.0
- R²: ~0.85-0.95
+ Biểu đồ regression
```

**Nhận xét**: Mạng BA tuân theo power-law (scale-free)

---

### **Bước 2.7: Visualization bố cục mạng**
```
✅ Cell: 4 network layouts
   - Spring layout (Force-directed)
   - Circular layout
   - Kamada-Kawai layout
   - Shell layout
```
**Output**: Figure với 4 subplots

---

### **Bước 2.8: Xuất file Gephi**
```
✅ Cell: Export GEXF
   nx.write_gexf(G, 'network_for_gephi.gexf')
```
**Output**: File `network_for_gephi.gexf`

---

## 🎯 LUỒNG 3: PHÂN TÍCH CẤU TRÚC (CENTRALITY)

### **Bước 3.1: Tính các độ đo trung tâm**
```
✅ Cell: Tính 4 centrality measures
   - Degree Centrality
   - Closeness Centrality
   - Betweenness Centrality
   - Eigenvector Centrality
```
**Output**: "✓ Đã tính toán xong tất cả các độ đo trung tâm!"

**Biến quan trọng**: 
- `degree_centrality`
- `closeness_centrality`
- `betweenness_centrality`
- `eigenvector_centrality`

---

### **Bước 3.2: Top nút trung tâm**
```
✅ Cell: Hiển thị top 10 nodes theo từng độ đo
```
**Output**: 4 bảng xếp hạng top 10

---

### **Bước 3.3: Thống kê mô tả**
```
✅ Cell: Tạo DataFrame centrality_df
   - describe() cho tất cả các độ đo
```
**Output**: Bảng thống kê (mean, std, min, max, quartiles)

**Biến quan trọng**: `centrality_df` (dùng cho các phân tích sau)

---

### **Bước 3.4: Visualization centrality**
```
✅ Cell: 8 biểu đồ (4 boxplot + 4 histogram)
```
**Output**: Figure với 2x4 subplots

---

### **Bước 3.5: PageRank và HITS**
```
✅ Cell: Tính PageRank (và HITS nếu có hướng)
   - Top 10 PageRank
```
**Output**: Bảng top 10 PageRank

**Cập nhật**: Thêm cột `PageRank` vào `centrality_df`

---

### **Bước 3.6: Ma trận tương quan**
```
✅ Cell: Correlation matrix + heatmap
```
**Output**: 
- Ma trận correlation
- Heatmap

**Phân tích**: Correlation giữa các độ đo (VD: Degree ↔ Betweenness)

---

### **Bước 3.7: Scatter plots**
```
✅ Cell: 6 scatter plots cho các cặp độ đo
   - Degree vs Betweenness
   - Degree vs Closeness
   - etc.
```
**Output**: Figure với 2x3 subplots (có regression lines)

---

### **Bước 3.8: Phân loại nút**
```
✅ Cell: Sắp xếp và phân loại
   - Hub nodes (cao cả degree & betweenness)
   - Bridge nodes (betweenness cao, degree thường)
   - Peripheral nodes (cả hai thấp)
```
**Output**: 
```
- Số nút Hub: ~15-20
- Số nút Bridge: ~30-40
- Số nút Peripheral: ~50-70
```

---

### **Bước 3.9: Tính tương đương cấu trúc**
```
✅ Cell: Jaccard similarity matrix
   - Top 20 nút có bậc cao
   - Heatmap similarity
   - Top 10 cặp tương đồng nhất
```
**Output**: Heatmap + bảng cặp tương đồng

---

## 👥 LUỒNG 4: PHÂN TÍCH CỘNG ĐỒNG

### **Bước 4.1: K-core decomposition**
```
✅ Cell: Tính k-core numbers
   - Phân phối k-core
   - Histogram + cumulative plot
```
**Output**: 
```
- K-core max: ~10-15
- Phân phối k-core
+ 2 biểu đồ
```

**Biến quan trọng**: `core_numbers`

---

### **Bước 4.2: Trích xuất k-core**
```
✅ Cell: Extract main core
   - Thống kê các k-core
   - Visualization (nếu nhỏ)
```
**Output**: Thông tin về main core

---

### **Bước 4.3: Phát hiện cộng đồng**
```
✅ Cell: Chạy 4 thuật toán
   1. Greedy Modularity
   2. Label Propagation
   3. Louvain (nếu có)
   4. Girvan-Newman (nếu mạng nhỏ)
```
**Output**: "✓ Hoàn thành phát hiện cộng đồng!"

**Biến quan trọng**: `community_results` (dict)

---

### **Bước 4.4: So sánh thuật toán**
```
✅ Cell: So sánh modularity
   - Bảng so sánh
   - 2 bar charts (số cộng đồng & modularity)
```
**Output**: 
```
Bảng so sánh:
- Greedy: X cộng đồng, modularity = 0.XX
- Label Prop: Y cộng đồng, modularity = 0.YY
- Louvain: Z cộng đồng, modularity = 0.ZZ (thường cao nhất)
+ 2 biểu đồ
```

**Biến quan trọng**: `best_communities`, `node_to_community`

---

### **Bước 4.5: Phân tích chi tiết cộng đồng**
```
✅ Cell: Phân tích cộng đồng tốt nhất
   - Top 10 cộng đồng lớn nhất
   - Histogram phân phối kích thước
   - Bar chart top communities
```
**Output**: 
```
Top 10 cộng đồng:
1. Cộng đồng 1: XX nút
2. Cộng đồng 2: YY nút
...
+ 2 biểu đồ
```

---

### **Bước 4.6: Visualization cộng đồng**
```
✅ Cell: Network layout với màu theo cộng đồng
   - All communities (màu khác nhau)
   - Top 5 communities (với label)
```
**Output**: Figure với 2 subplots

---

### **Bước 4.7: Xuất Gephi với cộng đồng**
```
✅ Cell: Export GEXF với thuộc tính community
```
**Output**: File `network_with_communities.gexf`

---

### **Bước 4.8: Phân tích inter-community**
```
✅ Cell: Phân tích mối quan hệ giữa các cộng đồng
   - Đếm cạnh intra-community vs inter-community
   - Ma trận kết nối giữa top communities
   - Heatmap
```
**Output**: 
```
- Cạnh trong cộng đồng: ~80%
- Cạnh giữa cộng đồng: ~20%
+ Heatmap ma trận kết nối
```

---

## 📝 LUỒNG 5: KẾT LUẬN

### **Bước 5.1: Tổng kết**
```
✅ Cell: Markdown - Tổng kết các phát hiện
   (Bạn tự điền dựa trên kết quả)
```

### **Bước 5.2: Tài liệu tham khảo**
```
✅ Cell: Markdown - References
```

---

## ✅ CHECKLIST CHẠY NOTEBOOK

### **Trước khi chạy:**
- [ ] Đã cài đặt packages: `pip install -r requirements.txt`
- [ ] Đã activate môi trường Python đúng
- [ ] Đã mở file notebook trong VS Code/Jupyter

### **Khi chạy:**
- [ ] Chạy theo thứ tự từ Cell 1 → Cell cuối
- [ ] Hoặc dùng "Run All Cells"
- [ ] Kiểm tra không có lỗi ở mỗi cell

### **Sau khi chạy:**
- [ ] Đã có 2 file .gexf trong thư mục
- [ ] Đã có tất cả biểu đồ hiển thị
- [ ] Biến `centrality_df` có đầy đủ dữ liệu
- [ ] Biến `best_communities` đã được tạo

---

## 🚨 THƯỜNG GẶP LỖI

### **Lỗi 1: NameError: name 'nx' is not defined**
**Nguyên nhân**: Chưa chạy cell import  
**Giải pháp**: Chạy cell "Import thư viện" trước

### **Lỗi 2: NameError: name 'G' is not defined**
**Nguyên nhân**: Chưa chạy cell tạo đồ thị  
**Giải pháp**: Chạy cell "Tạo đồ thị BA" trước

### **Lỗi 3: KeyError trong DataFrame**
**Nguyên nhân**: Chưa chạy cell tính centrality  
**Giải pháp**: Chạy cell "Tính các độ đo trung tâm" trước

### **Lỗi 4: ModuleNotFoundError: python-louvain**
**Nguyên nhân**: Chưa cài package  
**Giải pháp**: `pip install python-louvain`

---

## 📊 KẾT QUẢ MONG ĐỢI CHO MẠNG BA (n=300, m=3)

### **Thống kê tổng quan:**
- Số nút: 300
- Số cạnh: ~894
- Mật độ: ~0.02
- Đường kính: 6-7
- Bán kính: 4
- Hệ số phân cụm: 0.03-0.05 (thấp)
- Độ dài đường đi TB: 3.5-4.5 (small-world)

### **Phân phối bậc:**
- Bậc trung bình: ~6
- Bậc max: 30-50
- Gamma: 2.5-3.0
- R²: 0.85-0.95

### **Cộng đồng (Louvain):**
- Số cộng đồng: 8-12
- Modularity: 0.45-0.55
- Cộng đồng lớn nhất: 50-80 nút

---

## 🎓 VÍ DỤ PHÂN TÍCH MẠNG BA

### **Ý nghĩa của mô hình BA:**
Mạng Barabási-Albert mô phỏng mạng xã hội thực tế vì:
1. **Preferential attachment**: Người có nhiều bạn bè dễ kết bạn mới hơn
2. **Scale-free**: Có vài người rất nổi tiếng (hub), nhiều người ít bạn
3. **Small-world**: Khoảng cách giữa mọi người đều ngắn ("6 bậc phân cách")

### **Ứng dụng:**
- Phân tích mạng Twitter (follower network)
- Phân tích mạng Facebook (friendship network)
- Phân tích mạng trích dẫn khoa học
- Phân tích mạng Internet (router connections)

---

**📌 Lưu ý:** File này là hướng dẫn chi tiết. Hãy chạy notebook theo đúng thứ tự này để đạt kết quả tốt nhất!
