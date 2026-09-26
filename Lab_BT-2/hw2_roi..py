# Yêu cầu người dùng nhập số liệu đầu vào
tong_von_ban_dau = float(input("Nhập tổng vốn ban đầu (Initial Investment): "))
tong_gia_tri_ban = float(input("Nhập tổng giá trị bán ra (Final Value): "))

# Tính lợi nhuận ròng (Net Profit)
loi_nhuan_rong = tong_gia_tri_ban - tong_von_ban_dau

# Tính tỷ lệ ROI (%)
# Tránh lỗi chia cho 0 nếu vốn ban đầu bằng 0
if tong_von_ban_dau != 0:
    roi = (loi_nhuan_rong / tong_von_ban_dau) * 100
else:
    roi = 0.0

# Hiển thị kết quả ra màn hình
print("\n--- KẾT QUẢ ĐẦU TƯ ---")
print(f"Lợi nhuận ròng (Net Profit): {loi_nhuan_rong:,.2f}")
print(f"Tỷ suất sinh lời (ROI): {roi:.2f}%")
