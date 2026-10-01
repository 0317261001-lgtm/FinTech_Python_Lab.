# 1. Nhập vào Họ Tên đầy đủ
ho_ten = input("Nhập vào Họ Tên đầy đủ: ")

# 2. Nhập vào Năm sinh
nam_sinh = input("Nhập vào Năm sinh: ")

# 3. Xử lý chuỗi để tạo mã ưu đãi
# Tách các từ trong họ tên thành một danh sách (list)
danh_sach_tu = ho_ten.split()

# Lấy từ cuối cùng trong danh sách (chính là Tên)
ten = danh_sach_tu[-1]

# Lấy tối đa 3 ký tự đầu của Tên và chuyển thành chữ in hoa
ba_chu_cai_dau = ten[0:3].upper()

# Tạo mã ưu đãi bằng F-string
ma_uu_dai = f"{ba_chu_cai_dau}-{nam_sinh}-VIP"

# In kết quả ra màn hình
print(f"Mã ưu đãi của bạn là: {ma_uu_dai}")
