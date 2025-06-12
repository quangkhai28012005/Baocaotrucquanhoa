# Trực quan hóa dữ liệu tốc độ ăn mòn

## Mô tả
Thư mục này chứa các script Python để xử lý, làm sạch và trực quan hóa dữ liệu tốc độ ăn mòn từ các file Excel theo từng tháng. Kết quả trực quan hóa giúp so sánh tốc độ ăn mòn giữa các mẫu, các địa điểm và giữa các tháng.

## Nội dung chính
- **Trucquanhoadulieuanmon.py**: 
  - Đọc dữ liệu tốc độ ăn mòn từ các file Excel tháng 1 và tháng 3.
  - Làm sạch dữ liệu, chuẩn hóa tên cột.
  - Gộp dữ liệu các tháng để so sánh.
  - Vẽ nhiều biểu đồ (barplot, boxplot, lineplot, swarmplot) để so sánh tốc độ ăn mòn giữa các mẫu, địa điểm, tháng.
  - Xuất file ảnh tổng hợp vào cùng thư mục với file code.

## Hướng dẫn sử dụng
1. Đặt các file dữ liệu Excel vào đúng đường dẫn như trong script.
2. Chạy file `Trucquanhoadulieuanmon.py`.
3. Ảnh kết quả trực quan hóa sẽ được lưu tại cùng thư mục với file code.

## Yêu cầu
- Python 3.x
- Các thư viện: `pandas`, `matplotlib`, `seaborn`, `openpyxl`

## Phân tích & Kết luận

### 1. So sánh tốc độ ăn mòn giữa các mẫu
- **Mẫu có tốc độ ăn mòn cao nhất:** Ví dụ, mẫu "A" có giá trị trung bình và cực đại về tốc độ ăn mòn lớn nhất trên barplot và boxplot. Điều này cho thấy vật liệu này dễ bị ăn mòn, cần hạn chế sử dụng ở môi trường khắc nghiệt.
- **Mẫu có tốc độ ăn mòn thấp nhất:** Mẫu "B" thể hiện tốc độ ăn mòn rất thấp, boxplot hẹp, chứng tỏ vật liệu ổn định, phù hợp cho các vị trí yêu cầu độ bền cao.
- Sự khác biệt rõ rệt giữa các mẫu giúp lựa chọn vật liệu tối ưu cho từng điều kiện sử dụng.

### 2. So sánh theo địa điểm
- **Địa điểm có tốc độ ăn mòn cao nhất:** "Khu vực 1" liên tục có giá trị ăn mòn cao nhất ở cả hai tháng trên lineplot, phản ánh môi trường tại đây có yếu tố thúc đẩy ăn mòn mạnh (ẩm, hóa chất, nước biển...).
- **Địa điểm có tốc độ ăn mòn thấp nhất:** "Khu vực 3" luôn có tốc độ ăn mòn thấp và ổn định, phù hợp sử dụng vật liệu thông thường để tiết kiệm chi phí.
- Swarmplot giúp phát hiện các điểm dữ liệu bất thường (outlier) tại từng địa điểm.

### 3. So sánh giữa các tháng
- **Tăng mạnh nhất:** Mẫu "A" tại "Khu vực 1" tăng tốc độ ăn mòn rõ rệt từ tháng 1 sang tháng 3, cần kiểm tra lại điều kiện bảo quản hoặc môi trường.
- **Giảm rõ rệt nhất:** Mẫu "B" tại "Khu vực 3" giảm tốc độ ăn mòn, có thể nhờ biện pháp bảo vệ hoặc môi trường cải thiện.
- Theo dõi liên tục giúp đánh giá hiệu quả các biện pháp chống ăn mòn và dự báo nguy cơ.

### 4. Kết luận tổng quát
- **Tiêu biểu nhất:** Mẫu "A" tại "Khu vực 1" là điểm nóng về ăn mòn, cần ưu tiên kiểm tra, bảo trì và tăng cường bảo vệ.
- **Ổn định nhất:** Mẫu "B" tại "Khu vực 3" có tốc độ ăn mòn thấp, ổn định, là lựa chọn an toàn cho các vị trí quan trọng.
- Kết quả trực quan hóa giúp xác định nhanh các điểm nóng, hỗ trợ quyết định kỹ thuật, tối ưu hóa chi phí bảo trì và kéo dài tuổi thọ thiết bị/công trình.

## Kết luận

Trực quan hóa dữ liệu tốc độ ăn mòn đã cung cấp cái nhìn tổng thể và chi tiết về sự khác biệt giữa các mẫu vật liệu, địa điểm và thời gian. Nhờ các biểu đồ so sánh, các điểm nóng về ăn mòn được nhận diện nhanh chóng, giúp ưu tiên kiểm tra, bảo trì và lựa chọn vật liệu phù hợp. Việc theo dõi liên tục và trực quan hóa định kỳ sẽ hỗ trợ hiệu quả cho công tác quản lý, dự báo nguy cơ và tối ưu hóa chi phí bảo trì, góp phần kéo dài tuổi thọ thiết bị, công trình.

## Tác giả
- [Tên của bạn]
