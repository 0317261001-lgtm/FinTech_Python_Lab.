# Nhập tổng thu nhập chịu thuế từ người dùng (đơn vị: triệu VNĐ)
thu_nhap = float(input("Nhập tổng thu nhập chịu thuế (triệu VNĐ): "))

# Khởi tạo biến thuế phải nộp
tien_thue = 0.0

# Dùng cấu trúc if-elif-else tính thuế lũy tiến từng phần
if thu_nhap <= 5:
    tien_thue = thu_nhap * 0.05
elif thu_nhap <= 10:
    # 5 triệu đầu tiên tính 5%, phần vượt 5 triệu tính 10%
    tien_thue = 5 * 0.05 + (thu_nhap - 5) * 0.10
elif thu_nhap <= 18:
    # 5 triệu đầu (5%), 5 triệu tiếp theo (10%), phần vượt 10 triệu tính 15%
    tien_thue = 5 * 0.05 + 5 * 0.10 + (thu_nhap - 10) * 0.15
else:
    # Các bậc trước cộng lại, phần vượt 18 triệu tính 20%
    tien_thue = 5 * 0.05 + 5 * 0.10 + 8 * 0.15 + (thu_nhap - 18) * 0.20

# In kết quả ra màn hình
print(f"Số tiền thuế TNCN phải nộp là: {tien_thue:.2f} triệu VNĐ")
