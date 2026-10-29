def calculate_emi(principal, annual_rate, months):
    # Bước 1: Tính lãi suất tháng (r) từ lãi suất năm
    r = annual_rate / 12
    
    # Bước 2: Áp dụng công thức tính EMI
    # EMI = P * [r * (1 + r)^n] / [(1 + r)^n - 1]
    numerator = r * ((1 + r) ** months)
    denominator = ((1 + r) ** months) - 1
    emi = principal * (numerator / denominator)
    
    # Bước 3: Tính tổng số tiền lãi phải trả trong toàn bộ chu kỳ
    # Tổng tiền lãi = (Số tiền EMI hàng tháng * số tháng) - Số tiền gốc ban đầu
    total_interest = (emi * months) - principal
    
    # Hàm trả về Tuple gồm 2 giá trị
    return emi, total_interest

# --- Kiểm tra với Test Case trong bài ---
# Định nghĩa các giá trị đầu vào
vay_goc = 1000000000  # 1 tỷ VNĐ
lai_suat_nam = 0.12   # 12%/năm
thoi_gian_thang = 12  # 12 tháng

# Sử dụng Unpacking để nhận 2 giá trị trả về từ hàm
tra_hang_thang, tong_lai = calculate_emi(vay_goc, lai_suat_nam, thoi_gian_thang)

# In kết quả ra màn hình (định dạng dấu phẩy phân tách phần nghìn và làm tròn số)
print(f"Trả mỗi tháng: {tra_hang_thang:,.0f} VNĐ | Tổng lãi phải trả: {tong_lai:,.0f} VNĐ")
