# Task On Progress

## Nhiệm vụ và trạng thái
- Bỏ lọc khoảng ngày; chỉnh bố cục bộ lọc; không tự cuộn khi thay đổi filter; cấu hình notebook và kiểm tra dự đoán.
- UI và cấu hình đã hoàn tất. Chạy mô hình/notebook thật đang bị Windows Application Control chặn DLL; chưa thể xác nhận dự đoán chạy thành công.

## Đã hoàn tất
- Bộ lọc trong vùng chính gồm ba cột: loại cửa hàng, năm, tháng; giữ reset, số bản ghi và trạng thái rỗng. Không còn date_input/filter_dates.
- Navigation chỉ cuộn lên đầu khi đổi không gian phân tích; guard revision ngăn cuộn lại khi HTML remount sau chỉnh filter.
- Logo dùng file Walmart-Logo-New.png có sẵn.
- run_project.py cung cấp setup/doctor/dashboard/notebook/execute. Đã cài dependency trong .venv, đăng ký kernel Python (Walmart) bằng --sys-prefix.
- requirements-notebook.txt, scripts/check_environment.py, scripts/execute_notebook.py: kiểm tra import/fit thật; chạy notebook lưu bản output riêng theo timestamp, không ghi đè nguồn.
- Notebook thật là Do_An/walmart_eda_model/3122410447_LTT.ipynb, không phải 3122401447_LTT.ipynb. Đã cấu hình kernel, đường dẫn dataset và artifact; không đổi thuật toán. Output lịch sử trong nguồn không phải kết quả chạy mới.
- Dashboard tự train khi bấm Tạo dự đoán, không phụ thuộc việc chạy notebook trước. UI thông báo riêng lỗi Application Control và lệnh doctor.
- README.md và architecture.md đã cập nhật theo kết quả xác minh.

## Kiểm tra đã thực hiện (2026-09-18)
- 9/9 kiểm tra Python UI/filter đã đạt; sau thay đổi thông báo lỗi, chạy lại hai kiểm tra lỗi (gồm một test mới) đều đạt. Tổng cộng 10 test Python đã được kiểm tra. Ranh giới model được giả lập trong test UI, không chứng minh huấn luyện thật.
- 4/4 test Node navigation đạt, gồm chạy lại cùng revision không cuộn và đổi revision có cuộn.
- 62 code cell notebook và script trợ giúp qua kiểm tra cú pháp Python.
- Lệnh setup cài thư viện và kernel thành công nhưng kết thúc lỗi ở doctor do pandas timestamps bị chặn.
- Lệnh execute khởi động kernel thành công; cell thứ 6 tìm đúng đường dẫn dataset/artifact rồi thất bại khi import pandas: DLL tzconversion bị Application Control chặn.
- Bản lỗi: artifacts/notebook/20260918-094736-634897/3122410447_LTT.failed.ipynb. Chưa sinh model/metric mới.
- Môi trường UI tạm cũng không import sklearn được: lỗi tại scipy.integrate._quadpack do cùng chính sách Windows.
- Server UI hiện tại http://127.0.0.1:8501 trả health ok; vẫn dùng môi trường tạm. Chưa chuyển server sang .venv vì pandas trong .venv đang bị chặn.
- Browser automation không khả dụng; vị trí cuộn thật và hình ảnh desktop/mobile còn cần xác minh. AppTest không kiểm tra pixel/CSS.

## Việc tiếp theo
1. Người quản trị thiết bị cần cho phép các thư viện Python chính thức theo chính sách Application Control của máy. Không tắt hoặc né chính sách bảo mật.
2. Chạy python run_project.py doctor; chỉ khi thành công mới chạy python run_project.py execute để xác minh notebook đầy đủ. Mở Jupyter bằng python run_project.py notebook, chọn kernel Python (Walmart).
3. Sau khi import/fit thành công, kiểm tra dự đoán thật trên dashboard; thời gian huấn luyện và metric mới còn cần xác minh.
4. Kiểm tra giao diện/scroll trong trình duyệt thật khi có browser khả dụng.

## Lưu ý tiếp nối
- Không sửa myvenv: launcher cũ trỏ Anaconda không còn tồn tại, Git đang theo dõi nhiều file môi trường này.
- .venv/ và artifacts/ đã được gitignore. Không coi dependency là code ứng dụng để quét repository.
- Giữ task_on_progress.md theo yêu cầu người dùng.

_Cập nhật: 2026-09-18_
