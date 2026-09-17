<div align="center">

# Walmart Sales Analytics

### Phân tích dữ liệu & dự báo doanh số bán lẻ

Đồ án môn Phân tích dữ liệu · Đại học Sài Gòn (SGU) · 2025

**Python · Pandas · Scikit-learn · Plotly · Streamlit**

[Tổng quan](#tong-quan) · [Dữ liệu](#du-lieu) · [Cài đặt](#cai-dat) · [Kết quả](#ket-qua)

</div>

---

<a id="tong-quan"></a>

## 01 — Tổng quan

Dự án phân tích doanh số hàng tuần của chuỗi cửa hàng **Walmart**, tìm hiểu xu hướng theo thời gian, sự khác biệt giữa các cửa hàng và mối liên hệ giữa doanh số với các yếu tố kinh tế, mùa vụ, ngày lễ.

Quy trình triển khai bao gồm khám phá dữ liệu (EDA), tiền xử lý, xây dựng đặc trưng, so sánh mô hình hồi quy và trình bày kết quả qua dashboard tương tác.

| Phạm vi | Nội dung |
| :--- | :--- |
| **Bài toán** | Phân tích và dự báo doanh số hàng tuần theo cửa hàng, bộ phận |
| **Biến mục tiêu** | `Weekly_Sales` |
| **Dữ liệu huấn luyện** | 421.570 bản ghi, 45 cửa hàng |
| **Notebook** | Khám phá dữ liệu, trực quan hóa và so sánh 4 mô hình hồi quy |
| **Ứng dụng** | Dashboard Streamlit gồm 7 trang phân tích và dự đoán |

**Khám phá nhanh:** [Notebook phân tích](Do_An/walmart_eda_model/3122410447_LTT.ipynb) · [Mã nguồn dashboard](Do_An/walmart_eda_model/streamlit_dashboard.py) · [Thư mục dữ liệu](Do_An/dataset/)

## 02 — Nội dung phân tích

| Chức năng | Nội dung chính |
| :--- | :--- |
| **Tổng quan** | Tổng doanh số, doanh số trung bình, số cửa hàng và số bộ phận |
| **Khám phá dữ liệu** | Thống kê, phân phối dữ liệu và bộ lọc theo loại cửa hàng, năm |
| **Phân tích thời gian** | Xu hướng doanh số và biến động theo các mốc thời gian |
| **Phân tích tương quan** | Mối liên hệ giữa doanh số với nhiệt độ, giá nhiên liệu và các chỉ số kinh tế |
| **Phân tích ngày lễ** | So sánh doanh số giữa tuần có ngày lễ và tuần thông thường |
| **Dự đoán** | Ước lượng doanh số hàng tuần bằng Gradient Boosting |
| **Hiệu suất cửa hàng** | So sánh doanh số và xem chi tiết theo bộ phận của từng cửa hàng |

<a id="du-lieu"></a>

## 03 — Dữ liệu

Bốn tệp CSV được lưu tại [`Do_An/dataset/`](Do_An/dataset/). Số dòng bên dưới không bao gồm dòng tiêu đề.

| Tệp | Số dòng | Vai trò |
| :--- | ---: | :--- |
| [`train.csv`](Do_An/dataset/train.csv) | 421.570 | Doanh số lịch sử theo cửa hàng, bộ phận và tuần; có `Weekly_Sales` |
| [`test.csv`](Do_An/dataset/test.csv) | 115.064 | Các bản ghi cần dự đoán; không có `Weekly_Sales` |
| [`stores.csv`](Do_An/dataset/stores.csv) | 45 | Thông tin loại cửa hàng (`Type`) và quy mô (`Size`) |
| [`features.csv`](Do_An/dataset/features.csv) | 8.190 | Nhiệt độ, giá nhiên liệu, khuyến mãi, CPI, thất nghiệp và cờ ngày lễ |

Dữ liệu doanh số được ghép với thông tin cửa hàng qua `Store`, sau đó ghép với bảng đặc trưng qua `Store`, `Date` và `IsHoliday`. Các đặc trưng thời gian như năm, tháng, tuần và quý được tạo từ `Date`.

> **Phân biệt tập dữ liệu:** `test.csv` không có doanh số thực tế. Việc đánh giá mô hình sử dụng phần dữ liệu được tách từ `train.csv`.

## 04 — Cấu trúc dự án

```text
LTT_DA/
├── README.md                         # Giới thiệu và hướng dẫn sử dụng
└── Do_An/
    ├── readme.md                      # Liên kết tải mô hình đã lưu
    ├── dataset/
    │   ├── train.csv
    │   ├── test.csv
    │   ├── stores.csv
    │   └── features.csv
    └── walmart_eda_model/
        ├── 3122410447_LTT.ipynb       # Notebook phân tích và huấn luyện
        ├── streamlit_dashboard.py    # Dashboard tương tác
        ├── requirements.txt          # Thư viện Python
        ├── all_metrics_comparison.png
        ├── actual_vs_predicted.png
        └── feature_importance.png
```

<a id="cai-dat"></a>

## 05 — Cài đặt & sử dụng

Cần có **Python**, **pip** và bản sao dự án trên máy. Thực hiện các lệnh dưới đây từ thư mục gốc `LTT_DA/`.

### Bước 1 · Tạo môi trường ảo

```bash
python -m venv myvenv
```

Kích hoạt trên **Windows PowerShell**:

```powershell
.\myvenv\Scripts\Activate.ps1
```

Kích hoạt trên **macOS / Linux**:

```bash
source myvenv/bin/activate
```

### Bước 2 · Cài đặt thư viện

```bash
python -m pip install -r Do_An/walmart_eda_model/requirements.txt
```

### Bước 3 · Khởi chạy dashboard

```bash
python -m streamlit run Do_An/walmart_eda_model/streamlit_dashboard.py
```

Mở địa chỉ **Local URL** được hiển thị trong terminal, sau đó chọn trang phân tích từ thanh điều hướng bên trái.

> Khi mở trang **Dự Đoán**, ứng dụng huấn luyện Gradient Boosting từ dữ liệu hiện có và lưu mô hình trong bộ nhớ đệm của Streamlit. Lần đầu có thể mất vài phút tùy cấu hình máy; dashboard không yêu cầu tải tệp mô hình `.pkl` trước.

### Chạy notebook phân tích

Cài thêm JupyterLab và mở notebook từ thư mục chứa nó để các đường dẫn `../dataset/` hoạt động đúng:

```bash
python -m pip install jupyterlab
cd Do_An/walmart_eda_model
python -m jupyterlab 3122410447_LTT.ipynb
```

Chọn kernel của môi trường vừa cài thư viện và chạy các ô theo thứ tự từ trên xuống. Notebook bao gồm cả huấn luyện mô hình nên thời gian chạy phụ thuộc cấu hình máy.

<a id="ket-qua"></a>

## 06 — Mô hình & kết quả minh họa

Notebook so sánh **Linear Regression**, **Lasso**, **Random Forest** và **Gradient Boosting**. Các chỉ số đánh giá gồm MAE, MSE, RMSE, R² và WMAE — sai số tuyệt đối trung bình có trọng số. Notebook lựa chọn mô hình tốt nhất theo WMAE và có bước lưu mô hình bằng `joblib`.

![Biểu đồ so sánh MAE, MSE, RMSE và R² của bốn mô hình hồi quy](Do_An/walmart_eda_model/all_metrics_comparison.png)

*Biểu đồ kết quả đã lưu trong dự án; đây không phải kết quả của một lần huấn luyện mới khi đọc tài liệu.*

<details>
<summary><strong>Xem thêm: giá trị thực tế so với dự đoán & mức độ quan trọng của đặc trưng</strong></summary>

### Giá trị thực tế so với dự đoán

![So sánh doanh số thực tế và doanh số dự đoán](Do_An/walmart_eda_model/actual_vs_predicted.png)

### Mức độ quan trọng của đặc trưng

![Mức độ quan trọng của các đặc trưng trong mô hình](Do_An/walmart_eda_model/feature_importance.png)

</details>

Liên kết tải mô hình đã lưu được ghi tại [`Do_An/readme.md`](Do_An/readme.md). Các tệp `.pkl` được loại khỏi Git theo cấu hình `.gitignore`.

## 07 — Thông tin học phần

| Thông tin | Chi tiết |
| :--- | :--- |
| **Trường** | Đại học Sài Gòn — Saigon University (SGU) |
| **Học phần** | Phân tích dữ liệu · 2025 |
| **Giảng viên** | Do Nhu Tai |
| **Nhóm** | 5 |
| **Sinh viên** | Lương Thanh Tuấn |
| **Mã số sinh viên** | 3122410447 |

---

<div align="center">

**Từ dữ liệu bán lẻ đến phân tích và dự báo doanh số.**

[Về đầu trang](#walmart-sales-analytics)

</div>
