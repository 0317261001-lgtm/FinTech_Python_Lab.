# --------------------------------------------------------------------------
# Bài tập 1: Mô phỏng Kế hoạch Tích lũy Hưu trí Tự động
# --------------------------------------------------------------------------

# 1. Khởi tạo các hằng số và biến số tài chính theo đề bài
tuoi = 25                           # Tuổi bắt đầu tích lũy
so_du = 0.0                         # Số dư tài sản đầu kỳ ban đầu (VNĐ)
tien_gui = 60000000.0               # Tiền gửi mới năm đầu tiên (VNĐ)
lai_suat = 0.10                     # Tỷ suất sinh lời đầu tư bình quân (10%/năm)
tang_tien_gui = 0.08                # Tỷ lệ tăng trưởng khoản tiền gửi (8%/năm)
muc_tieu = 10000000000.0            # Mục tiêu tài sản đạt được để nghỉ hưu (10 tỷ VNĐ)

nam_tich_luy = 0                    # Biến đếm số năm tích lũy
tuoi_ban_dau = tuoi                 # Lưu lại tuổi ban đầu để tính toán kết luận

# Hàm bổ trợ định dạng tiền tệ chuyên nghiệp có dấu phẩy phân cách hàng nghìn
def format_money(amount):
    return f"{amount:,.0f} VNĐ"

# 2. In tiêu đề bảng báo cáo theo mẫu kết quả xuất ra
print("===== BÁO CÁO MÔ PHỎNG KẾ HOẠCH HƯU TRÍ TỰ ĐỘNG =====")
print(f"Mục tiêu tài sản: {format_money(muc_tieu)}\n")

# Định dạng các cột tiêu đề của bảng
header = f"{'Năm':<5} | {'Tuổi':<5} | {'Tiền gửi mới':<18} | {'Tiền lãi phát sinh':<20} | {'Dư nợ/Tài sản cuối năm'}"
print(header)
print("-" * len(header))

# 3. Vòng lặp mô phỏng quá trình tích lũy qua từng năm
# Điều kiện dừng: Vòng lặp chạy liên tục cho đến khi số dư tài sản cuối năm đạt hoặc vượt mục tiêu
while so_du < muc_tieu:
    nam_tich_luy += 1               # Tăng biến đếm số năm tích lũy thêm 1
    
    # Tính toán các giá trị tài chính phát sinh trong năm t
    tien_lai_trong_nam = so_du * lai_suat
    so_du_cuoi_nam = so_du + tien_lai_trong_nam + tien_gui
    
    # In thông tin tiến trình của năm hiện tại ra màn hình
    print(f"{nam_tich_luy:<5} | {tuoi:<5} | {format_money(tien_gui):<18} | {format_money(tien_lai_trong_nam):<20} | {format_money(so_du_cuoi_nam)}")
    
    # Cập nhật giá trị chuẩn bị cho năm tiếp theo
    so_du = so_du_cuoi_nam          # Số dư cuối năm nay trở thành số dư đầu kỳ năm sau
    tien_gui = tien_gui * (1 + tang_tien_gui)  # Tiền gửi mới năm sau tăng 8% so với năm nay
    tuoi += 1                       # Tuổi tăng thêm 1
    
print("-" * len(header))

# 4. In kết luận cuối cùng sau khi hoàn thành mục tiêu hưu trí
print(f"KẾT LUẬN: Khách hàng sẽ đạt mục tiêu nghỉ hưu sau {nam_tich_luy} năm (lúc {tuoi_ban_dau + nam_tich_luy} tuổi).")
