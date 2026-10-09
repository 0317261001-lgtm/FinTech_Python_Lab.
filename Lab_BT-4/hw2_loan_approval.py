# 1. Khai báo và khởi tạo dữ liệu giả định để kiểm tra (Có thể thay đổi để test)
has_bad_debt = False          # True: có nợ xấu, False: không có nợ xấu
monthly_income = 20000000     # Thu nhập hàng tháng (VNĐ)
monthly_payment = 8000000     # Số tiền trả góp hàng tháng (VNĐ)

print("--- HỆ THỐNG THẨM ĐỊNH HỒ SƠ VAY MUA NHÀ ---")

# Bước 1: Check CIC (Kiểm tra nợ xấu)
if has_bad_debt:
    print("Kết quả: TỪ CHỐI VAY.")
    print("Lý do: Khách hàng có lịch sử nợ xấu trên hệ thống CIC.")
else:
    # Bước 2: Check Thu nhập (Nếu không có nợ xấu mới chạy vào đây)
    if monthly_income < 15000000:
        print("Kết quả: TỪ CHỐI VAY.")
        print("Lý do: Thu nhập không đủ hạn mức tối thiểu (< 15,000,000 VNĐ).")
    else:
        # Bước 3: Check Tỷ lệ DTI (Nếu thu nhập >= 15 triệu mới chạy vào đây)
        # Tính ngưỡng trả góp tối đa cho phép (50% thu nhập)
        max_allowed_payment = monthly_income * 0.5
        
        if monthly_payment <= max_allowed_payment:
            print("Kết quả: DUYỆT KHOẢN VAY.")
            print(f"Lý do: Tài chính an toàn. Tỷ lệ DTI hợp lệ (Trả góp: {monthly_payment:,} VNĐ / Thu nhập: {monthly_income:,} VNĐ).")
        else:
            print("Kết quả: TỪ CHỐI VAY.")
            print("Lý do: Tỷ lệ rủi ro tài chính vượt mức cho phép (Số tiền trả góp vượt quá 50% thu nhập).")
