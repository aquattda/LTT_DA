# HƯỚNG DẪN NHANH - PHÂN TÍCH MẠNG XÃ HỘI

## Bước 1: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

Hoặc cài thủ công:

```bash
pip install networkx pandas numpy matplotlib seaborn scipy python-louvain
```

## Bước 2: Chạy notebook

### Option A: VS Code (khuyến nghị)
1. Mở file `sma.ipynb` trong VS Code
2. Chọn Python kernel (myvenv hoặc Python 3.x)
3. Chạy cell đầu tiên để import thư viện
4. Chạy các cell tiếp theo theo thứ tự

### Option B: Jupyter Notebook
```bash
jupyter notebook sma.ipynb
```

### Option C: Jupyter Lab
```bash
jupyter lab sma.ipynb
```

## Bước 3: Chuẩn bị dữ liệu

**Nếu dùng dữ liệu mẫu (đơn giản nhất):**
- Không cần làm gì, code đã sẵn sàng!
- Mạng Barabasi-Albert với 300 nút sẽ được tạo tự động

**Nếu dùng dữ liệu của bạn:**

### Format 1: File CSV (edge list)
```csv
source,target
Alice,Bob
Bob,Charlie
Charlie,Alice
...
```

Code để load:
```python
edges_df = pd.read_csv('your_data.csv')
G = nx.from_pandas_edgelist(edges_df, source='source', target='target')
```

### Format 2: File TXT (edge list)
```
Alice Bob
Bob Charlie
Charlie Alice
...
```

Code để load:
```python
G = nx.read_edgelist('your_data.txt')
```

### Format 3: File với trọng số
```csv
source,target,weight
Alice,Bob,5
Bob,Charlie,3
...
```

Code để load:
```python
edges_df = pd.read_csv('your_data.csv')
G = nx.from_pandas_edgelist(edges_df, source='source', target='target', 
                            edge_attr='weight', create_using=nx.Graph())
```

### Format 4: Mạng có hướng
```python
G = nx.from_pandas_edgelist(edges_df, source='source', target='target', 
                            create_using=nx.DiGraph())
```

## Bước 4: Hiểu kết quả

### Phần 2: Tổng quan mạng
- **Mật độ**: Gần 0 = thưa, gần 1 = dày đặc
- **Đường kính**: Khoảng cách lớn nhất giữa 2 nút bất kỳ
- **Hệ số phân cụm**: >0.5 = nhóm chặt, <0.2 = rời rạc
- **Power-law gamma**: 2-3 = mạng scale-free điển hình

### Phần 3: Cấu trúc mạng
- **Degree Centrality**: Số kết nối trực tiếp
- **Betweenness**: Vai trò cầu nối
- **Closeness**: Khả năng tiếp cận nhanh
- **Eigenvector**: Kết nối với nút quan trọng

### Phần 4: Cộng đồng
- **Modularity**: >0.3 = có cộng đồng rõ ràng
- **Số cộng đồng**: Phụ thuộc thuật toán
- Best method: Thường là Louvain hoặc Greedy

## Bước 5: Xuất kết quả

Notebook sẽ tự động tạo:
- `network_for_gephi.gexf` - Đồ thị cơ bản
- `network_with_communities.gexf` - Đồ thị có cộng đồng

**Import vào Gephi:**
1. File > Open > Chọn file .gexf
2. Overview tab > Layout > ForceAtlas 2 > Run
3. Appearance:
   - Nodes > Size > Ranking > degree
   - Nodes > Color > Partition > community
4. Preview tab > Adjust settings > Export PNG/SVG

## Xử lý lỗi thường gặp

### Lỗi 1: Module not found
```bash
pip install <tên_module>
```

### Lỗi 2: NetworkX version cũ
```bash
pip install --upgrade networkx
```

### Lỗi 3: Eigenvector centrality không converge
- Đổi `max_iter=1000` thành `max_iter=5000`
- Hoặc bỏ qua Eigenvector cho mạng này

### Lỗi 4: Girvan-Newman quá lâu
- Bình thường, thuật toán này chậm
- Có thể comment out phần Girvan-Newman nếu mạng >200 nút

### Lỗi 5: Out of memory
- Mạng quá lớn
- Giảm kích thước mạng bằng sampling
- Hoặc dùng server/máy mạnh hơn

## Tips

### Tăng tốc cho mạng lớn
1. Bỏ qua Girvan-Newman
2. Sử dụng approximate betweenness:
```python
betweenness_centrality = nx.betweenness_centrality(G, k=100)  # Sample 100 nodes
```

### Visualization đẹp hơn
1. Dùng Gephi thay vì matplotlib
2. Điều chỉnh tham số layout:
```python
pos = nx.spring_layout(G, k=1.0, iterations=100)  # k càng lớn càng rộng
```

### Lưu kết quả phân tích
```python
# Lưu centrality measures
centrality_df.to_csv('centrality_results.csv', index=False)

# Lưu community assignments
community_df = pd.DataFrame({
    'Node': list(node_to_community.keys()),
    'Community': list(node_to_community.values())
})
community_df.to_csv('community_assignments.csv', index=False)
```

## Checklist hoàn thành bài tập

- [ ] Import thư viện thành công
- [ ] Load dữ liệu (mẫu hoặc của bạn)
- [ ] Chạy phần 2: Tổng quan mạng
- [ ] Chạy phần 3: Cấu trúc mạng
- [ ] Chạy phần 4: Phân tích cộng đồng
- [ ] Xuất file .gexf
- [ ] Import vào Gephi và tạo visualization
- [ ] Hoàn thành phần Kết luận
- [ ] Chuẩn bị slide thuyết trình (nếu cần)

## Thời gian ước tính

- Setup: 10 phút
- Chạy notebook (mạng 300 nút): 2-5 phút
- Visualization Gephi: 15 phút
- Viết kết luận: 30 phút
- **Tổng: ~1 giờ**

---

**Nếu gặp vấn đề, check lại:**
1. Python version >= 3.8
2. Tất cả thư viện đã cài đặt
3. Dữ liệu format đúng
4. Đủ RAM (recommend 4GB+)
5. Đọc error message kỹ càng

**Good luck! 🚀**
