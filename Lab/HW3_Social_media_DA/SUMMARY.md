# BẢNG TÓM TẮT - CÁC PHÂN TÍCH TRONG NOTEBOOK

## 📊 Phần 2: Phân tích Tổng quan Mạng

| Phân tích | Công cụ/Hàm | Ý nghĩa | Thời gian |
|-----------|-------------|---------|-----------|
| Kiểu đồ thị | `nx.is_directed()`, `nx.is_weighted()` | Xác định loại mạng | <1s |
| Số nút/cạnh | `G.number_of_nodes()`, `G.number_of_edges()` | Kích thước mạng | <1s |
| Mật độ | `nx.density()` | Mức độ kết nối (0-1) | <1s |
| Đường kính | `nx.diameter()` | Khoảng cách max giữa 2 nút | O(n²) |
| Bán kính | `nx.radius()` | Khoảng cách min đến tất cả | O(n²) |
| Hệ số phân cụm | `nx.clustering()` | Xu hướng tạo nhóm | O(n) |
| Độ dài đường đi TB | `nx.average_shortest_path_length()` | Hiệu quả lan truyền | O(n²) |
| Phân phối bậc | `G.degree()` | Phân bố kết nối | O(n) |
| Hồi quy Power-law | `scipy.stats.linregress()` | Tính scale-free | O(n log n) |

**Output:**
- Thống kê số liệu
- 10+ biểu đồ (histogram, boxplot, log-log plot)
- 2 file GEXF cho Gephi

---

## 🎯 Phần 3: Phân tích Cấu trúc Mạng

### 3.1 Các Độ đo Trung tâm

| Độ đo | Hàm | Ý nghĩa | Complexity | Phù hợp cho |
|-------|-----|---------|------------|-------------|
| **Degree** | `nx.degree_centrality()` | Số kết nối trực tiếp | O(n) | Influencer, Hub |
| **Closeness** | `nx.closeness_centrality()` | Gần các nút khác | O(n²) | Broadcaster |
| **Betweenness** | `nx.betweenness_centrality()` | Cầu nối giữa nhóm | O(n³) | Bridge, Gatekeeper |
| **Eigenvector** | `nx.eigenvector_centrality()` | Kết nối nút quan trọng | O(n²) | Prestigious |
| **PageRank** | `nx.pagerank()` | Quan trọng (có hướng) | O(n) | Authority |
| **HITS** | `nx.hits()` | Hub & Authority | O(n²) | Web, Citation |

**Output:**
- Top 10 nút cho mỗi độ đo
- Bảng thống kê mô tả
- 8 biểu đồ visualization
- Ma trận tương quan (heatmap)
- 6 scatter plots so sánh

### 3.2 Phân loại Nút

| Loại | Đặc điểm | Vai trò |
|------|----------|---------|
| **Hub** | Degree cao + Betweenness cao | Trung tâm kết nối |
| **Bridge** | Betweenness cao + Degree thấp | Cầu nối giữa nhóm |
| **Peripheral** | Cả hai đều thấp | Ngoại vi, ít quan trọng |

### 3.3 Tương đồng Cấu trúc

- **Jaccard Similarity**: So sánh láng giềng chung
- **Heatmap**: Top 20 nút có bậc cao
- **Pairs**: Top 10 cặp nút tương đồng nhất

---

## 🏘️ Phần 4: Phân tích Cộng đồng

### 4.1 K-core Decomposition

| Metric | Công thức | Ý nghĩa |
|--------|-----------|---------|
| K-core | Subgraph với min degree ≥ k | Tìm core mạng |
| Main core | Max k-core | Nhân mạng chặt nhất |

**Output:**
- Phân phối k-core
- Histogram + Cumulative
- Visualization main core (nếu <100 nút)

### 4.2 Thuật toán Phát hiện Cộng đồng

| Thuật toán | Complexity | Pros | Cons | Khuyến nghị |
|------------|------------|------|------|-------------|
| **Greedy Modularity** | O(n log²n) | Nhanh, modularity cao | Bỏ lỡ nhóm nhỏ | ✅ Luôn dùng |
| **Label Propagation** | O(m+n) | Rất nhanh | Không deterministic | ✅ Mạng lớn |
| **Louvain** | O(n log n) | Tốt nhất, phổ biến | Cần cài đặt | ⭐ Khuyến nghị |
| **Girvan-Newman** | O(m²n) | Hierarchical | Rất chậm | ⚠️ Chỉ mạng nhỏ |

**Các chỉ số đánh giá:**

| Chỉ số | Công thức | Ý nghĩa | Ngưỡng tốt |
|--------|-----------|---------|------------|
| **Modularity** | Q = Σ[eᵢᵢ - aᵢ²] | Chất lượng phân vùng | >0.3 |
| **Coverage** | Cạnh trong nhóm / tổng | % cạnh nội bộ | >0.7 |
| **Performance** | Σ correct pairs / total | Độ chính xác | >0.8 |

**Output:**
- Bảng so sánh 3-4 thuật toán
- 2 biểu đồ so sánh (số cộng đồng, modularity)
- Top 10 cộng đồng lớn nhất
- 2 visualizations (toàn bộ + top 5)
- Ma trận kết nối giữa các cộng đồng

---

## 📈 Tổng kết Output

### Files xuất ra:
1. `network_for_gephi.gexf` - Đồ thị cơ bản
2. `network_with_communities.gexf` - Đồ thị + cộng đồng

### Visualizations tạo ra:
- **Phần 2:** 8 biểu đồ
- **Phần 3:** 15 biểu đồ
- **Phần 4:** 10 biểu đồ
- **Tổng:** ~33 biểu đồ

### Thống kê xuất ra:
- Bảng thống kê mô tả: 5 bảng
- Bảng so sánh: 3 bảng
- DataFrame centrality: 1 file
- Community assignments: 1 file

---

## ⏱️ Thời gian chạy ước tính

| Kích thước mạng | Phần 2 | Phần 3 | Phần 4 | Tổng |
|-----------------|--------|--------|--------|------|
| 50 nút | 5s | 10s | 5s | 20s |
| 100 nút | 10s | 30s | 10s | 50s |
| 300 nút | 20s | 90s | 30s | 2.5m |
| 500 nút | 40s | 180s | 60s | 5m |
| 1000 nút | 90s | 600s | 180s | 15m |
| 5000 nút | 600s | 3600s+ | 900s | 60m+ |

**Lưu ý:**
- Thời gian phụ thuộc vào cấu hình máy
- Betweenness và Girvan-Newman là bottleneck chính
- Với mạng >1000 nút, nên dùng approximate algorithms

---

## 🎓 Diễn giải Kết quả

### Phân phối Bậc

| Hình dạng | Mô hình | Ví dụ |
|-----------|---------|-------|
| Bell curve | Random (Erdős-Rényi) | Mạng ngẫu nhiên |
| Power-law | Scale-free (Barabási-Albert) | Internet, Citation |
| Exponential | Small-world (Watts-Strogatz) | Mạng xã hội |

### Hệ số Phân cụm

| Giá trị | Ý nghĩa | Loại mạng |
|---------|---------|-----------|
| >0.7 | Rất chặt, nhiều triangle | Mạng bạn bè |
| 0.3-0.7 | Trung bình | Mạng xã hội |
| <0.3 | Thưa, ít nhóm | Mạng ngẫu nhiên |

### Modularity

| Q | Ý nghĩa | Hành động |
|---|---------|-----------|
| >0.7 | Cộng đồng rất rõ | Excellent |
| 0.4-0.7 | Cộng đồng khá rõ | Good |
| 0.3-0.4 | Có cộng đồng | Acceptable |
| <0.3 | Không có cộng đồng rõ | Try other methods |

### Tương quan Centralities

| Correlation | Ý nghĩa |
|-------------|---------|
| Degree ↔ Betweenness cao | Hub cũng là bridge |
| Degree ↔ Betweenness thấp | Có bridge riêng biệt |
| Degree ↔ Eigenvector cao | Hub kết nối với hub |
| Closeness ↔ Betweenness cao | Bridge có vị trí tốt |

---

## 🔧 Customization Options

### Điều chỉnh Layout:
```python
# Thay đổi k trong spring_layout
pos = nx.spring_layout(G, k=0.5)  # Mặc định
pos = nx.spring_layout(G, k=1.0)  # Rộng hơn
pos = nx.spring_layout(G, k=0.1)  # Compact hơn
```

### Điều chỉnh Ngưỡng phân loại:
```python
# Từ quantile 0.75 -> 0.9 cho ngưỡng cao hơn
degree_threshold = centrality_df['Degree_Centrality'].quantile(0.9)
```

### Approximate Algorithms (cho mạng lớn):
```python
# Betweenness với sampling
betweenness = nx.betweenness_centrality(G, k=100)  # Sample 100 nodes

# Closeness cho mạng lớn
closeness = nx.closeness_centrality(G, distance='weight')
```

---

## 📚 Tài liệu tham khảo

1. **NetworkX:** https://networkx.org/documentation/stable/
2. **Gephi:** https://gephi.org/users/
3. **Books:**
   - Network Science by Barabási
   - Networks by Newman
4. **Papers:**
   - Blondel et al. (2008) - Louvain method
   - Girvan & Newman (2002) - Community detection

---

**Chúc bạn phân tích thành công! 🎉**
