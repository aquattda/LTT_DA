# Architecture Memory

## Project overview
- Đồ án phân tích và dự đoán doanh số hàng tuần Walmart theo cửa hàng/bộ phận. Hai luồng Python riêng: notebook EDA/so sánh mô hình và dashboard Streamlit tương tác.
- Dashboard đọc CSV và huấn luyện model riêng; không nạp `.pkl` của notebook và không cần chạy notebook trước. Notebook đã được cấu hình kernel/đường dẫn chạy; CSV và thuật toán model giữ nguyên.
- Đường dẫn tính từ root; cell notebook đánh số từ 0 trong mảng `cells`.

## Công nghệ và dependency
- `Do_An/walmart_eda_model/requirements.txt`: Streamlit >=1.52 (hỗ trợ JavaScript qua st.html), pandas, NumPy, Plotly, Seaborn, Matplotlib, scikit-learn, joblib, statsmodels; chưa ghim phiên bản chính xác.
- Dashboard trực quan hóa bằng Plotly, xử lý bằng pandas/NumPy. scikit-learn chỉ được import khi gọi `train_model()`, để lỗi thư viện model không chặn các trang phân tích.
- `requirements-notebook.txt` bao gồm requirements dashboard, scipy, JupyterLab, ipykernel, nbconvert và nbclient. `run_project.py setup` tạo `.venv` và đăng ký kernel `walmart` / `Python (Walmart)` trong chính môi trường này.
- Đã chạy AppTest bằng Python 3.12 với Streamlit 1.64.0, pandas 3.0.5, Plotly 7.1.0, NumPy 2.5.3. Đây là môi trường kiểm tra UI, không xác nhận toàn bộ môi trường ML.

## Entry points và module
| File / symbol | Vai trò |
|---|---|
| `Do_An/walmart_eda_model/streamlit_dashboard.py` / `main()` | Entry point Streamlit; đọc dữ liệu, sidebar, điều phối 7 trang |
| `streamlit_dashboard.py` / `load_data()`, `train_model()` | Cache dữ liệu CSV và model Gradient Boosting |
| `streamlit_dashboard.py` / `sidebar()`, `PAGES`, `filter_bar()` | Sidebar điều hướng; ba bộ lọc Type/Year/Month trong nội dung chính |
| `streamlit_dashboard.py` / `overview_page`, `eda_page`, `time_analysis_page`, `correlation_page`, `holiday_analysis_page`, `prediction_page`, `store_performance_page` | Bảy nhóm phân tích |
| `Do_An/walmart_eda_model/dashboard_ui.py` | Palette, nhãn, định dạng tiền, header, KPI, panel, theme Plotly, thông báo |
| `Do_An/walmart_eda_model/navigation.js` | Cuộn main container và document về đầu sau khi render trang mới |
| `Do_An/walmart_eda_model/Walmart-Logo-New.png` | Logo do người dùng cung cấp, nhúng nguyên bytes qua data URI vào sidebar |
| `Do_An/walmart_eda_model/dashboard.css` | Bố cục responsive; sidebar navy, nền sáng, accent teal; panel dùng class từ key của st.container |
| `.streamlit/config.toml` | Theme app/sidebar; được đọc khi chạy từ root |
| `Do_An/walmart_eda_model/3122410447_LTT.ipynb` | Entry point Jupyter: EDA, tiền xử lý, so sánh model, xuất ảnh/model |
| `run_project.py` | CLI setup/doctor/dashboard/notebook/execute dùng interpreter `.venv`, không cần activate shell |
| `scripts/check_environment.py`, `scripts/execute_notebook.py` | Kiểm tra dependency + fit/predict nhỏ thực; chạy toàn notebook, lưu output riêng và dừng khi cell lỗi |
| `Do_An/dataset/` | Bốn CSV đầu vào |
| `tests/test_dashboard.py` | unittest + Streamlit AppTest, dùng CSV thật và model giả lập tại ranh giới dự đoán |
| `tests/test_dashboard_filters.py`, `tests/test_navigation.cjs` | AppTest cho bộ lọc/logo/navigation; kiểm tra JavaScript bằng DOM giả lập trong Node |
| `README.md`, `Do_An/readme.md`, `assets/readme/` | Tổng quan/cách chạy, link model, hình trang trí và ảnh kết quả |

## Dữ liệu, lưu trữ, tích hợp
- train.csv: Store, Dept, Date, Weekly_Sales, IsHoliday. test.csv không có Weekly_Sales.
- stores.csv: Store, Type, Size. features.csv: Store/Date, Temperature, Fuel_Price, MarkDown1–5, CPI, Unemployment, IsHoliday.
- `load_data()` xác định `../dataset` từ `__file__`; left join stores theo Store rồi features theo Store/Date/IsHoliday. Tạo Year/Month/Week/Quarter; fill MarkDown1–5 bằng 0, thêm CPI/Unemployment cho test.
- Dữ liệu ở filesystem và DataFrame trong RAM; `st.cache_data` cache kết quả đọc, `st.cache_resource` cache model. Không thấy database/API nghiệp vụ trong các luồng đã khảo sát.
- `prediction_result` trong session_state lưu kịch bản đã gửi và kết quả; đổi form không gán nhãn mới cho kết quả cũ. Dashboard không ghi model ra file.
- Trang cửa hàng cho tải CSV tổng hợp theo bộ lọc; không gửi dữ liệu tới dịch vụ ngoài.
- `Do_An/readme.md` chứa link Google Drive tải model thủ công; dashboard không dùng. Nội dung/quyền truy cập: **cần xác minh**.
- `.gitignore` có quy tắc myvenv và *.pkl, nhưng Git vẫn theo dõi nhiều file trong myvenv. Không khảo sát thư viện đó như code ứng dụng, tránh tạo thay đổi bytecode tại đây.

## Luồng UI và ý nghĩa chỉ số
1. `main()` nạp dữ liệu, `sidebar()` chỉ chọn trang. `filter_bar()` nằm dưới tiêu đề, bố cục ba cột: Type, Year, một Month hoặc tất cả. Không có filter khoảng ngày. Các điều kiện kết hợp; khi không có bản ghi hiện thông báo; reset khôi phục toàn bộ phạm vi. State bộ lọc được giữ khi chuyển qua trang dự đoán (trang này dùng toàn bộ train).
2. Overview: doanh số tổng; doanh số trung bình **toàn hệ thống/tuần**; số Store/Dept duy nhất; xu hướng tuần; donut tỷ trọng doanh số theo Type; top Dept theo trung bình bản ghi; bảng cửa hàng dùng nunique, không đếm dòng.
3. EDA: histogram tính bằng NumPy trên toàn dữ liệu; box plot dùng quartile và fence tính sẵn, không truyền hàng trăm nghìn điểm ra UI; ma trận Pearson.
4. Thời gian: chuyển tuần/tháng, mùa vụ theo tháng, quý và loại cửa hàng qua năm. Tổng kỳ chưa đủ có chú thích không so sánh trực tiếp.
5. Tương quan: hệ số trên toàn dữ liệu lọc, scatter lấy tối đa 3.000 dòng với random_state=42; trung bình chỉ số kinh tế loại trùng Store/Date trước khi gộp tháng.
6. Ngày lễ: phân nhóm theo IsHoliday; an toàn khi thiếu nhóm hoặc thiếu tuần 45–52. Không coi tương quan/chênh lệch mô tả là nhân quả.
7. Hiệu suất cửa hàng: cộng các bộ phận theo Store/Date rồi tính trung bình tuần toàn cửa hàng; chỉ số USD/tuần/1.000 ft² dùng trung bình này chia Size × 1.000. Có bảng, tải CSV và chi tiết Dept.
8. Biểu đồ và các chỉ số ghi rõ cấp tổng hợp, dùng `dashboard_ui.py` và CSS chung, không tải font/asset từ mạng.
9. `scroll_to_top_on_navigation()` chỉ phát script khi đổi trang. Ngoài kiểm tra page ở Python, `navigation.js` lưu revision trên window để HTML remount không cuộn lặp khi chỉnh filter. Hai requestAnimationFrame chờ render rồi scroll main/document/window; đổi filter không phát scroll. Test có cả tình huống chạy lại cùng script; vị trí cuộn trình duyệt thật còn cần xác minh.

## Dự đoán
- Chỉ train khi người dùng gửi form. Constructor giữ GradientBoostingRegressor(n_estimators=100, max_depth=15, learning_rate=0.1, random_state=42).
- Type dùng LabelEncoder, IsHoliday dùng int; loại dòng thiếu đặc trưng; train/validation ngẫu nhiên 80/20, random_state=42.
- 12 đặc trưng: Store, Dept, Size, Type_encoded, Temperature, Fuel_Price, CPI, Unemployment, IsHoliday_encoded, Year, Month, Week.
- Lựa chọn Dept giới hạn theo Store; diện tích mặc định theo cửa hàng. Nhiệt độ/giá nhiên liệu/CPI/thất nghiệp lấy trung bình lịch sử; Month ước lượng từ Week như luồng cũ.
- Test CSV chỉ bổ sung tập năm cho UI, không có dự đoán hàng loạt. R² hiển thị là validation random split, không phải kiểm định theo thời gian.
- Lỗi dependency được thông báo trong UI; lỗi chi tiết được ghi server log. Chưa xác minh dự đoán thực trong môi trường kiểm tra bị Windows chặn binary sklearn.

## Notebook
- File thực là `3122410447_LTT.ipynb`; không có file `3122401447_LTT.ipynb` trong checkout khảo sát.
- Cell 5 xác định PROJECT_ROOT từ WALMART_PROJECT_ROOT hoặc cwd/parents; DATASET_DIR trỏ Do_An/dataset. Các cell 11, 16, 21, 25 dùng DATASET_DIR; không phụ thuộc đường dẫn tương đối ../dataset. Merge (31, 33, 38, 40), đặc trưng thời gian (45, 48), EDA giữ nguyên.
- Fill thiếu, mã hóa Type/IsHoliday, bỏ một số cột trước train (105, 110, 116–120, 135–136). Tiền xử lý khác dashboard.
- Chia train/validation 80/20 (141); so sánh Linear Regression, Lasso, Random Forest, Gradient Boosting; MAE/MSE/RMSE/R²/WMAE và thời gian (145). WMAE trọng số tuần lễ 5, tuần thường 1 (143).
- Chọn WMAE nhỏ nhất (147), xuất ba ảnh (150, 152, 154) và model qua joblib.dump (156) vào OUTPUT_DIR. Chạy thủ công mặc định artifacts/notebook/manual; CLI execute truyền WALMART_OUTPUT_DIR theo timestamp cho mỗi lần chạy, tránh ghi đè artifact cũ.
- CLI execute dùng kernel walmart, working directory root, timeout mỗi cell 1800 giây, không bỏ qua lỗi. Xóa output lịch sử trong bản chạy, lưu `.executed.ipynb` hoặc `.failed.ipynb`; không ghi đè notebook nguồn.
- Artifact có sẵn không chứng minh một lần chạy mới.

## Chạy và kiểm tra
Từ root repository, trong môi trường Python có dependency:

```powershell
python run_project.py setup
python run_project.py doctor
python run_project.py dashboard
python run_project.py notebook
python run_project.py execute
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
node --test tests/test_navigation.cjs
```

- Test UI dùng model giả lập cho submit/result/error, kiểm tra số liệu thật cho bộ lọc và doanh số cửa hàng; không đo chất lượng model.
- Test JavaScript dùng node:test tích hợp, không cần cài package npm. API st.html hỗ trợ thực thi script từ Streamlit 1.52: https://docs.streamlit.io/develop/quick-reference/release-notes/2025#version-1520.
- Không có build riêng, lint/CI chưa được cấu hình. CLI luôn chạy từ root để nhận theme; runtime/config Jupyter, IPython và Matplotlib nằm trong `.venv/runtime/`. Kernel được đăng ký với --sys-prefix, không sửa kernel toàn máy.
- `.venv/` và `artifacts/` được gitignore. Script không sửa chính sách bảo mật Windows; doctor báo lỗi import/fit thực thay vì xác nhận giả.

## Cần xác minh / giới hạn
- **Cần xác minh:** ảnh giao diện desktop/mobile và tương tác trình duyệt thực; AppTest không kiểm tra pixel/CSS. Browser tích hợp không khả dụng, agent-browser bị Windows Application Control chặn trong phiên thiết kế.
- **Cần xác minh:** dự đoán với sklearn thực, tái lập metric/model notebook, dữ liệu đầy đủ và hiệu quả dự báo theo thời gian. Windows Application Control chặn các DLL: môi trường UI tạm lỗi tại scipy.integrate._quadpack; môi trường .venv mới lỗi pandas timestamps/tzconversion. Đây là lỗi thực thi của máy, không phải thiếu lần chạy notebook.
- **Đã xác minh (2026-09-18):** .venv đã cài dependency và đăng ký kernel Python (Walmart). Lệnh execute khởi động kernel, xác định đúng đường dẫn dataset/artifact rồi dừng ở cell code đầu tiên (cell thứ 6) khi import pandas do Application Control. Chưa có model/metric mới; bản lỗi được lưu tại artifacts/notebook/20260918-094736-634897/3122410447_LTT.failed.ipynb. Cần quản trị thiết bị cho phép các thư viện chính thức theo chính sách của máy rồi chạy doctor/execute lại.
- **Đã xác minh:** launcher myvenv hiện trỏ Anaconda không còn tồn tại. Môi trường kiểm tra UI được tạo riêng trong thư mục tạm; không sửa myvenv.
- Devcontainer còn trỏ `Lab/[HW2] Xay dung financial dashboard/vn30_dashboard.py` không có trong checkout và requirements ở root sai vị trí; chưa sửa do ngoài phạm vi UI. Deployment thực tế: **cần xác minh**.

_Cập nhật: 2026-09-18_
