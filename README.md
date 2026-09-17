<a id="top"></a>

<p align="center">
  <img src="assets/readme/walmart-hero.png" alt="Walmart Sales Analytics — Explore patterns. Predict possibilities." width="100%" />
</p>

<div align="center">

**PHÂN TÍCH DỮ LIỆU & DỰ BÁO DOANH SỐ BÁN LẺ**

Từ dữ liệu của 45 cửa hàng đến mô hình hồi quy và dashboard tương tác.

**[Khám phá notebook ↗](Do_An/walmart_eda_model/3122410447_LTT.ipynb)** &nbsp; · &nbsp; **[Chạy dashboard →](#quick-start)** &nbsp; · &nbsp; **[Xem kết quả ↓](#results)**

<sub>Đại học Sài Gòn · Phân tích dữ liệu · Nhóm 5 · 2025</sub>

</div>

<br />

![421.570 bản ghi huấn luyện · 45 cửa hàng · 4 mô hình hồi quy · 7 trang dashboard](assets/readme/project-stats.svg)

<br />

## ◈ &nbsp; Bài toán

**Doanh số thay đổi như thế nào — và có thể dự đoán đến đâu?**

Dự án khám phá doanh số hàng tuần của chuỗi cửa hàng **Walmart**: nhận diện xu hướng theo thời gian, so sánh hiệu suất cửa hàng và tìm hiểu mối liên hệ với ngày lễ, khuyến mãi cùng các yếu tố kinh tế. Biến mục tiêu là **`Weekly_Sales`**, được phân tích theo từng cửa hàng và bộ phận.

<p align="center">
  <a href="#experience">Dashboard</a> &nbsp; / &nbsp;
  <a href="#workflow">Quy trình</a> &nbsp; / &nbsp;
  <a href="#results">Mô hình</a> &nbsp; / &nbsp;
  <a href="#data">Dữ liệu</a> &nbsp; / &nbsp;
  <a href="#quick-start">Cài đặt</a> &nbsp; / &nbsp;
  <a href="#structure">Cấu trúc</a>
</p>

<br />

<a id="experience"></a>

## ⌘ &nbsp; Một bộ dữ liệu. Nhiều góc nhìn.

<table>
<tr>
<td width="50%" valign="top">
<h3>01 &nbsp; Khám phá kinh doanh</h3>
<p>Tổng quan doanh số, phân phối dữ liệu và hiệu suất từng cửa hàng, bộ phận.</p>
<sub>OVERVIEW · EDA · STORE PERFORMANCE</sub>
</td>
<td width="50%" valign="top">
<h3>02 &nbsp; Đọc xu hướng thời gian</h3>
<p>Theo dõi biến động doanh số, yếu tố mùa vụ và sự khác biệt giữa tuần có ngày lễ với tuần thông thường.</p>
<sub>TIME ANALYSIS · HOLIDAY ANALYSIS</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3>03 &nbsp; Tìm mối liên hệ</h3>
<p>Khám phá tương quan của doanh số với nhiệt độ, giá nhiên liệu, CPI và tỷ lệ thất nghiệp.</p>
<sub>CORRELATION · ECONOMIC FEATURES</sub>
</td>
<td width="50%" valign="top">
<h3>04 &nbsp; Thử nghiệm dự đoán</h3>
<p>Chọn cửa hàng, bộ phận và các đầu vào để ước lượng doanh số hàng tuần bằng Gradient Boosting.</p>
<sub>MACHINE LEARNING · SALES PREDICTION</sub>
</td>
</tr>
</table>

<br />

<a id="workflow"></a>

## ⤷ &nbsp; Từ dữ liệu đến dự đoán

![Quy trình: thu thập dữ liệu → khám phá → tiền xử lý → huấn luyện và đánh giá → dashboard](assets/readme/workflow.svg)

Ghép dữ liệu theo **cửa hàng, ngày và cờ ngày lễ**; xử lý giá trị thiếu; tạo đặc trưng thời gian; so sánh mô hình hồi quy và trình bày phân tích trên Streamlit.

![Công nghệ: Python · Pandas · Scikit-learn · Plotly · Streamlit](assets/readme/tech-stack.svg)

<details>
<summary><strong>Các thư viện hỗ trợ</strong></summary>

NumPy hỗ trợ tính toán; Matplotlib và Seaborn phục vụ biểu đồ trong notebook; Statsmodels hỗ trợ phân tích thống kê; Joblib dùng để lưu mô hình. Xem danh sách tại [`requirements.txt`](Do_An/walmart_eda_model/requirements.txt).

</details>

<br />

<a id="results"></a>

## ◇ &nbsp; Model showcase

**Bốn mô hình. Cùng một bài toán dự báo.**

`Linear Regression` &nbsp; `Lasso` &nbsp; `Random Forest` &nbsp; `Gradient Boosting`

Notebook so sánh mô hình bằng **MAE · MSE · RMSE · R² · WMAE** và chọn mô hình tốt nhất theo **WMAE** — sai số tuyệt đối trung bình có trọng số.

<p align="center">
  <img src="Do_An/walmart_eda_model/all_metrics_comparison.png" alt="Kết quả so sánh MAE, MSE, RMSE và R² của bốn mô hình hồi quy" width="850" />
</p>

<p align="center"><sub>Kết quả thực nghiệm đã lưu trong dự án, không phải số liệu từ một lần huấn luyện mới.</sub></p>

<details>
<summary><strong>↗ &nbsp; Mở bộ biểu đồ đánh giá chi tiết</strong></summary>

### Thực tế so với dự đoán

![So sánh doanh số thực tế và doanh số dự đoán](Do_An/walmart_eda_model/actual_vs_predicted.png)

### Mức độ quan trọng của đặc trưng

![Mức độ quan trọng của các đặc trưng](Do_An/walmart_eda_model/feature_importance.png)

</details>

<details>
<summary><strong>↗ &nbsp; Mô hình đã lưu & cách dashboard dự đoán</strong></summary>

Notebook có bước lưu mô hình bằng `joblib`. Liên kết tải mô hình nằm trong [`Do_An/readme.md`](Do_An/readme.md); các tệp `.pkl` được loại khỏi Git.

Dashboard sử dụng **Gradient Boosting**, tự huấn luyện khi mở trang **Dự Đoán** và lưu mô hình trong bộ nhớ đệm Streamlit. Không cần tải tệp `.pkl` để chạy dashboard; lần huấn luyện đầu có thể mất vài phút tùy máy.

</details>

<br />

<a id="data"></a>

## ▤ &nbsp; Bên trong bộ dữ liệu

| Nguồn | Số bản ghi | Nội dung |
| :--- | ---: | :--- |
| [`train.csv`](Do_An/dataset/train.csv) | **421.570** | Doanh số theo cửa hàng, bộ phận và tuần; có `Weekly_Sales` |
| [`test.csv`](Do_An/dataset/test.csv) | **115.064** | Các bản ghi cần dự đoán; không có doanh số thực tế |
| [`stores.csv`](Do_An/dataset/stores.csv) | **45** | Loại và quy mô cửa hàng |
| [`features.csv`](Do_An/dataset/features.csv) | **8.190** | Nhiệt độ, nhiên liệu, khuyến mãi, CPI, thất nghiệp, ngày lễ |

> **Ghi chú đánh giá:** tập dùng để đánh giá mô hình được tách từ `train.csv`. Tệp `test.csv` không chứa `Weekly_Sales`. Số bản ghi trong bảng không bao gồm tiêu đề.

<br />

<a id="quick-start"></a>

## ↗ &nbsp; Khởi chạy dự án

Có **Python** và **pip**, mở terminal tại thư mục gốc `LTT_DA/`.

### 01 / Chuẩn bị môi trường

```bash
python -m venv myvenv
```

<details open>
<summary><strong>Windows · PowerShell</strong></summary>

```powershell
.\myvenv\Scripts\Activate.ps1
```

</details>

<details>
<summary><strong>macOS / Linux</strong></summary>

```bash
source myvenv/bin/activate
```

</details>

### 02 / Cài thư viện & mở dashboard

```bash
python -m pip install -r Do_An/walmart_eda_model/requirements.txt
python -m streamlit run Do_An/walmart_eda_model/streamlit_dashboard.py
```

Mở **Local URL** trong terminal và chọn một trong **7 trang** ở thanh điều hướng bên trái.

<details>
<summary><strong>↗ &nbsp; Chạy notebook phân tích bằng JupyterLab</strong></summary>

Từ thư mục gốc dự án, trong môi trường đã cài các thư viện ở trên:

```bash
python -m pip install jupyterlab
cd Do_An/walmart_eda_model
python -m jupyterlab 3122410447_LTT.ipynb
```

Chọn kernel của môi trường vừa cài và chạy các ô theo thứ tự. Giữ thư mục làm việc tại `Do_An/walmart_eda_model/` để đường dẫn `../dataset/` hoạt động đúng. Các bước huấn luyện có thể cần nhiều thời gian tùy cấu hình máy.

</details>

<br />

<a id="structure"></a>

## ⌁ &nbsp; Project map

```text
LTT_DA/
├── README.md
├── assets/readme/                  # Bộ nhận diện cho README
└── Do_An/
    ├── readme.md                   # Liên kết tải mô hình
    ├── dataset/                    # train · test · stores · features
    └── walmart_eda_model/
        ├── 3122410447_LTT.ipynb    # Phân tích & huấn luyện
        ├── streamlit_dashboard.py # Dashboard tương tác
        ├── requirements.txt       # Thư viện Python
        ├── all_metrics_comparison.png
        ├── actual_vs_predicted.png
        └── feature_importance.png
```

<br />

---

<div align="center">

<sub>THE PERSON BEHIND THE PROJECT</sub>

### Lương Thanh Tuấn

**3122410447** &nbsp; / &nbsp; Nhóm 5 &nbsp; / &nbsp; Đại học Sài Gòn

Giảng viên: **Do Nhu Tai** · Học phần Phân tích dữ liệu · **2025**

<br />

**EXPLORE PATTERNS. PREDICT POSSIBILITIES.**

<sub>[↑ Về đầu trang](#top)</sub>

</div>
