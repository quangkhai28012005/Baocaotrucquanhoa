# Trực quan hóa dữ liệu thời tiết

## Mô tả
Dự án này tổng hợp, làm sạch và trực quan hóa dữ liệu thời tiết từ nhiều file CSV của các thành phố khác nhau. Kết quả trực quan hóa giúp so sánh các đặc trưng thời tiết như nhiệt độ, độ ẩm, lượng mưa, số giờ nắng giữa các thành phố và theo từng tháng.

## Các bước chính
1. **Tổng hợp dữ liệu**: Đọc tất cả file CSV trong thư mục dữ liệu, gộp thành một file tổng hợp.
2. **Làm sạch dữ liệu**: 
   - Tự động nhận diện cột ngày tháng.
   - Loại bỏ các dòng thiếu dữ liệu quan trọng.
   - Loại bỏ các giá trị bất hợp lý.
3. **Tính toán tổng hợp**: Tính trung bình/thống kê các chỉ số theo tháng và thành phố.
4. **Trực quan hóa**: 
   - Biểu đồ so sánh giữa các thành phố (nhiệt độ, độ ẩm, lượng mưa, số giờ nắng, phân phối, scatter plot).
   - Biểu đồ riêng cho từng thành phố (barplot theo tháng).
5. **Xuất file ảnh**: Các biểu đồ được lưu vào cùng thư mục với file code.

## Cách sử dụng
- Đặt các file dữ liệu CSV vào thư mục `Dữ liệu thời tiết đã tổng hợp`.
- Chạy file `Dulieuthoitiet.py` để tự động tổng hợp, làm sạch và xuất các file ảnh trực quan hóa.
- Các file ảnh kết quả sẽ nằm cùng thư mục với file code.

## Yêu cầu
- Python 3.x
- Các thư viện: `pandas`, `matplotlib`, `seaborn`

## Kết luận

Qua các biểu đồ trực quan hóa, có thể rút ra một số nhận xét chính:

- **Nhiệt độ trung bình** giữa các thành phố có sự khác biệt rõ rệt theo mùa và vị trí địa lý. Một số thành phố có biên độ nhiệt lớn hơn các thành phố khác.
- **Độ ẩm trung bình** thường biến động ngược chiều với nhiệt độ, đặc biệt vào các tháng mùa hè hoặc mùa mưa.
- **Lượng mưa tổng hợp** cho thấy các thành phố ven biển hoặc miền núi có lượng mưa cao hơn vào một số thời điểm trong năm, phản ánh đặc trưng khí hậu vùng miền.
- **Số giờ nắng trung bình** giúp nhận diện các thành phố có khí hậu khô ráo, nhiều nắng hoặc thường xuyên nhiều mây.
- **Phân phối nhiệt độ** qua boxplot cho thấy mức độ ổn định hoặc biến động của thời tiết từng thành phố.
- **Mối quan hệ giữa nhiệt độ và độ ẩm** thể hiện rõ qua scatter plot, giúp nhận diện các điều kiện thời tiết cực đoan.

Nhìn chung, trực quan hóa giúp so sánh, đánh giá và nhận diện các đặc trưng khí hậu của từng thành phố một cách trực quan, hỗ trợ cho việc phân tích, dự báo hoặc ra quyết định liên quan đến thời tiết.

## Tác giả
- [Tên của bạn]
