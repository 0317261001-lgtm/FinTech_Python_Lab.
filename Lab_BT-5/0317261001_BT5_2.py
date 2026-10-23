# --- 1. KHỞI TẠO CÁC BIẾN SỐ THEO ĐỀ BÀI CHỈ ĐỊNH ---
F = 1000000.0       # Mệnh giá trái phiếu (F)
c = 0.09            # Lãi suất coupon hàng năm (c = 9%)
N = 10              # Thời hạn trái phiếu (N = 10 năm)
y = 0.085           # Tỷ lệ lợi suất kỳ vọng thị trường (y = YTM = 8.5%)

# --- 2. TÍNH TOÁN CÁC GIÁ TRỊ CƠ BẢN ---
C = F * c           # Số tiền lãi coupon trả hàng năm

# --- 3. IN TIÊU ĐỀ BÁO CÁO (Theo phong cách bài tập 1) ---
print("===== BÁO CÁO TỰ ĐỘNG HÓA ĐỊNH GIÁ TRÁI PHIẾU DOANH NGHIỆP =====")
print(f"Mệnh giá (F): {F:,.0f} VNĐ | Lãi suất coupon: {c*100:.1f}%/năm")
print(f"Thời hạn (N): {N} năm     | Lợi suất kỳ vọng (y): {y*100:.1f}%/năm\n")

# In tiêu đề bảng chiết khấu dòng tiền lãi coupon từng năm
print(f"{'Năm (t)':<7} | {'Tiền lãi Coupon (C)':<22} | {'Giá trị hiện tại PV_coupon'}")
print("-" * 65)

# Khởi tạo biến tích lũy tổng giá trị hiện tại của các khoản coupon
tong_pv_coupon = 0.0

# --- 4. VÒNG LẶP FOR KẾT HỢP RANGE() ĐỂ CHIẾT KHẤU DÒNG TIỀN ---
for t in range(1, N + 1):
    # Công thức tính PV của khoản lãi coupon tại năm t
    pv_c = C / ((1 + y) ** t)
    
    # Cộng dồn vào tổng giá trị hiện tại của dòng coupon
    tong_pv_coupon += pv_c
    
    # In chi tiết từng năm được căn lề thẳng hàng theo cấu trúc bài 1
    print(f"{t:<7} | {C:>17,.0f} VNĐ | {pv_c:>22,.2f} VNĐ")

print("-" * 65)

# --- 5. TÍNH GIÁ TRỊ HIỆN TẠI CỦA MỆNH GIÁ GỐC VÀ GIÁ TRỊ TRÁI PHIẾU ---
pv_f = F / ((1 + y) ** N)
gia_trai_phieu = tong_pv_coupon + pv_f

# --- 6. IN KẾT QUẢ VÀ ĐÁNH GIÁ TRẠNG THÁI (PREMIUM / PAR / DISCOUNT) ---
print(f"Tổng giá trị hiện tại của lãi Coupon: {tong_pv_coupon:,.2f} VNĐ")
print(f"Giá trị hiện tại của nợ gốc (PV_f):   {pv_f:,.2f} VNĐ")
print(f"Giá lý thuyết chuẩn trái phiếu (P0):  {gia_trai_phieu:,.2f} VNĐ")
print("-" * 65)

# Cấu trúc rẽ nhánh đánh giá trạng thái giá phát hành
if gia_trai_phieu > F:
    trang_thai = "Cao hơn mệnh giá (Premium)"
elif gia_trai_phieu == F:
    trang_thai = "Đúng mệnh giá (Par)"
else:
    trang_thai = "Thấp hơn mệnh giá (Discount)"

print(f"KẾT LUẬN: Trái phiếu này đang được bán: {trang_thai}")
