# Nhập thông tin từ bàn phím
ten_san_pham = input("Nhập tên sản phẩm: ")
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá: "))

# Tính toán các giá trị theo công thức
tong_tien_hang = so_luong * don_gia
thue_vat = tong_tien_hang * 0.08
tong_thanh_toan = tong_tien_hang + thue_vat

# In hóa đơn bán hàng với định dạng hiển thị số tiền :,.0f
print("\n========== HÓA ĐƠN BÁN HÀNG ==========")
print(f"Tên sản phẩm:     {ten_san_pham}")
print(f"Số lượng:         {so_luong}")
print(f"Đơn giá:          {don_gia:,.0f}đ")
print("--------------------------------------")
print(f"Tổng tiền hàng:   {tong_tien_hang:,.0f}đ")
print(f"Thuế VAT (8%):    {thue_vat:,.0f}đ")
print("--------------------------------------")
print(f"Tổng thanh toán:  {tong_thanh_toan:,.0f}đ")
print("======================================")
