def credit_score(income, credit_history_years, has_bad_debt=False):
    if has_bad_debt:
        return "Reject"
    if income < 10000000 or credit_history_years < 1:
        return "High Risk"
    if income >= 20000000 and credit_history_years >= 3:
        return "VIP"
    return "Standard"

# --- CHỈ NHẬP THU NHẬP VÀ SỐ NĂM ---
print("--- CHƯƠNG TRÌNH CHẤM ĐIỂM TÍN DỤNG ---")

income = int(input("Nhập thu nhập hàng tháng (VND): "))
credit_history_years = int(input("Nhập số năm lịch sử tín dụng: "))

# Khi gọi hàm, không truyền has_bad_debt thì nó sẽ tự động lấy bằng False
ket_qua = credit_score(income, credit_history_years)

print(f"\n=> Phân hạng tín dụng: {ket_qua}")
