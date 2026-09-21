# 1. Yêu cầu người dùng nhập thông tin
ho_ten = input("Nhập họ tên khách hàng: ")
so_dien_thoai = input("Nhập số điện thoại: ")
cccd = input("Nhập số Căn cước công dân (CCCD): ")
so_tien_nap = float(input("Nhập số tiền nạp ban đầu (VND): "))

# 2. Định nghĩa chi phí và tính toán số dư
PHI_MO_VI = 50000
so_du_kha_dung = so_tien_nap - PHI_MO_VI

# 3. Xử lý chuỗi theo yêu cầu
ho_ten_in_hoa = ho_ten.upper()  # In hoa toàn bộ họ tên
b_so_cuoi_cccd = cccd[-4:]      # Cắt lấy 4 số cuối của CCCD

# 4. In biên lai khởi tạo ví
print("\n" + "="*30)
print("BIÊN LAI KHỞI TẠO VÍ ĐIỆN TỬ")
print("="*30)
print(f"Họ tên khách hàng: {ho_ten_in_hoa}")
print(f"Số điện thoại:    {so_dien_thoai}")
print(f"4 số cuối CCCD:   {b_so_cuoi_cccd}")
print(f"Số tiền nạp:      {so_tien_nap:,.0f} VND")
print(f"Phí mở ví:        {PHI_MO_VI:,.0f} VND")
print("-"*30)
print(f"SỐ DƯ KHẢ DỤNG:   {so_du_kha_dung:,.0f} VND")
print("="*30)
