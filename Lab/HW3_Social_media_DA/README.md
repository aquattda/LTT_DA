# Bài tập Phân tích Mạng Xã hội

**Sinh viên:** Lương Thanh Tuấn  
**MSSV:** 3122410447

## Mô tả

Notebook này cung cấp phân tích toàn diện về mạng xã hội, bao gồm:

1. **Phân tích tổng quan mạng**
   - Thông tin cơ bản (số nút, cạnh, mật độ)
   - Đường kính và bán kính
   - Hệ số phân cụm
   - Độ dài đường đi trung bình
   - Phân phối bậc và mô hình power-law
   - Bố cục mạng

2. **Phân tích cấu trúc mạng**
   - Các độ đo trung tâm (Degree, Closeness, Betweenness, Eigenvector)
   - PageRank và HITS (cho mạng có hướng)
   - So sánh tương quan giữa các độ đo
   - Phân loại nút (Hub, Bridge, Peripheral)
   - Phân tích tính tương đương cấu trúc

3. **Phân tích cộng đồng**
   - K-core decomposition
   - So sánh các thuật toán phát hiện cộng đồng:
     - Greedy Modularity
     - Label Propagation
     - Louvain (nếu có cài đặt)
     - Girvan-Newman (cho mạng nhỏ)
   - Visualization cộng đồng
   - Phân tích mối quan hệ giữa các cộng đồng

## Yêu cầu

### Thư viện Python

```bash
pip install networkx pandas numpy matplotlib seaborn scipy
```

### Thư viện tùy chọn (khuyến nghị)

```bash
# Để sử dụng thuật toán Louvain
pip install python-louvain

# Để export/import với Gephi
# (NetworkX đã hỗ trợ sẵn định dạng GEXF)
```

## Cách sử dụng

### Bước 1: Chuẩn bị dữ liệu

Bạn có 3 lựa chọn:

**Option 1:** Sử dụng dữ liệu mẫu (đã có sẵn trong code)
- Mạng Barabasi-Albert (300 nút) - Mặc định
- Karate Club (34 nút)
- Les Miserables (77 nút)

**Option 2:** Load dữ liệu từ file
- Đọc từ file CSV (edge list)
- Đọc từ file TXT (edge list)
- Đọc từ file GML, GraphML, GEXF

**Option 3:** Thu thập dữ liệu từ API mạng xã hội
- Facebook API
- Twitter API
- Instagram API
- v.v.

### Bước 2: Chạy notebook

1. Mở file `sma.ipynb` trong Jupyter Notebook hoặc VS Code
2. Chạy lần lượt các cell từ đầu đến cuối
3. Uncomment phần load dữ liệu phù hợp với nguồn dữ liệu của bạn

### Bước 3: Visualization nâng cao với Gephi

Notebook sẽ xuất 2 file:
- `network_for_gephi.gexf` - Đồ thị cơ bản
- `network_with_communities.gexf` - Đồ thị có thông tin cộng đồng

**Hướng dẫn sử dụng Gephi:**

1. Tải Gephi: https://gephi.org/
2. Mở file GEXF trong Gephi: `File > Open`
3. Chọn Layout:
   - ForceAtlas 2 (khuyến nghị)
   - Fruchterman Reingold
   - OpenOrd
4. Appearance panel:
   - Nodes > Ranking > degree (để điều chỉnh size)
   - Nodes > Partition > community (để tô màu theo cộng đồng)
5. Run Statistics:
   - Modularity (để xác nhận cộng đồng)
   - Average Degree
   - Network Diameter
6. Export ảnh: `File > Export > PNG/SVG`

## Cấu trúc file

```
HW3_Social_media_DA/
├── sma.ipynb                           # Notebook chính
├── README.md                           # File này
├── network_for_gephi.gexf             # File xuất cho Gephi (tạo khi chạy)
└── network_with_communities.gexf      # File có thông tin cộng đồng (tạo khi chạy)
```

## Kết quả chính

Khi chạy notebook, bạn sẽ có:

1. **Các chỉ số thống kê:**
   - Số nút, số cạnh, mật độ
   - Đường kính, bán kính
   - Hệ số phân cụm
   - Độ dài đường đi trung bình
   - Phân phối bậc

2. **Danh sách các nút quan trọng:**
   - Top nút theo các độ đo trung tâm
   - Hub nodes, Bridge nodes
   - Nút trung tâm và ngoại vi

3. **Thông tin cộng đồng:**
   - Số lượng cộng đồng
   - Kích thước các cộng đồng
   - Modularity score
   - Ma trận kết nối giữa các cộng đồng

4. **Visualizations:**
   - Histogram và boxplot
   - Scatter plots
   - Heatmaps
   - Network layouts
   - Community visualizations

## Ghi chú

### Về hiệu năng

- Một số phép tính có thể mất thời gian với mạng lớn (>1000 nút):
  - Betweenness Centrality: O(n³)
  - Girvan-Newman: O(m²n)
  - Closeness Centrality: O(n²)

- Khuyến nghị:
  - Với mạng >500 nút: Bỏ qua Girvan-Newman
  - Với mạng >1000 nút: Sử dụng sampling hoặc approximate algorithms

### Về visualization

- Python matplotlib phù hợp cho mạng nhỏ (<100 nút)
- Gephi phù hợp cho mạng trung bình đến lớn (100-10000 nút)
- Cytoscape là lựa chọn khác cho visualization chuyên nghiệp

### Về thuật toán phát hiện cộng đồng

**Greedy Modularity:**
- Ưu: Nhanh, modularity cao
- Nhược: Có thể bỏ lỡ cộng đồng nhỏ

**Label Propagation:**
- Ưu: Rất nhanh, gần tuyến tính O(m+n)
- Nhược: Kết quả không deterministic

**Louvain:**
- Ưu: Nhanh, modularity rất cao, phổ biến nhất
- Nhược: Cần cài đặt thêm package

**Girvan-Newman:**
- Ưu: Kết quả hierarchical, có thể chọn số cộng đồng
- Nhược: Rất chậm O(m²n)

## Tùy chỉnh

### Thay đổi ngưỡng phân loại nút

Trong phần 3.4, bạn có thể điều chỉnh:

```python
degree_threshold = centrality_df['Degree_Centrality'].quantile(0.75)  # Thay 0.75 -> 0.8 cho ngưỡng cao hơn
betweenness_threshold = centrality_df['Betweenness_Centrality'].quantile(0.75)
```

### Thay đổi số top communities hiển thị

```python
top_n_comms = min(10, len(best_communities))  # Thay 10 -> 15 để hiển thị nhiều hơn
```

### Thay đổi layout algorithm

```python
# Trong visualization
pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)

# Thử các layout khác:
pos = nx.kamada_kawai_layout(G)
pos = nx.circular_layout(G)
pos = nx.shell_layout(G)
```

## Tài liệu tham khảo

1. **NetworkX Documentation:** https://networkx.org/documentation/stable/
2. **Gephi Tutorials:** https://gephi.org/users/
3. **Books:**
   - Barabási, A. L. (2016). *Network Science*. Cambridge University Press.
   - Newman, M. E. (2018). *Networks*. Oxford University Press.
4. **Papers:**
   - Blondel et al. (2008). Fast unfolding of communities in large networks
   - Girvan & Newman (2002). Community structure in social and biological networks

## Liên hệ

Nếu có câu hỏi, vui lòng liên hệ:
- Email: [email của bạn]
- GitHub: [github của bạn]

---

**Good luck với bài tập! 🎉**
