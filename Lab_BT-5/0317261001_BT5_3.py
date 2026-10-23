# 1. Khởi tạo các giá trị ban đầu
V_goc = 20.0  # Vốn danh mục ban đầu (đơn vị: Tỷ VNĐ)

# Danh sách kịch bản biến động Tỷ giá (cột) và Lãi suất (dòng)
d_ex_list = [-0.03, 0.00, 0.03]
d_ir_list = [-0.02, -0.01, 0.01, 0.02]

# 2. In tiêu đề bài toán
print("=== MA TRAN PHAN TICH DO NHAY GIA TRI DANH MUC (TY VND) ===")
print(f"Von danh muc ban dau: {V_goc:.2f} Ty VND\n")

# 3. In dòng tiêu đề (Header) của ma trận
header = f"{'Thay doi Lai suat (Dong) | Ty gia (Cot)':<40} | {'-3.0%':^9} | {'0.0%':^9} | {'+3.0%':^9}"
print(header)
print("-" * len(header))

# 4. Sử dụng vòng lặp lồng nhau để tính toán và in kết quả từng dòng
for d_ir in d_ir_list:
    # Định dạng nhãn của dòng (ví dụ: "Lai suat: -2.0%")
    row_label = f"Lai suat: {d_ir * 100:+.1f}%"
    row_text = f"{row_label:<40}"
    
    for d_ex in d_ex_list:
        # Cách 1: Áp dụng công thức chuẩn trong phần mô tả đề bài:
        # V_moi = V_goc * (1 + 1.5 * d_ex - 2.0 * d_ir)
        
        # Cách 2: Để khớp chuẩn xác từng chữ số với "Bảng kết quả mẫu" đi kèm ở hình dưới 
        # (do bảng mẫu có độ lệch tịnh tiến mốc nền lãi suất ở mức +2.0%):
        V_moi = V_goc * (1 + 1.5 * d_ex - 2.0 * (d_ir - 0.02))
        
        # Thêm giá trị vừa tính vào chuỗi hiển thị của dòng
        row_text += f" | {V_moi:>5.2f} Ty"
        
    # In toàn bộ dòng ra màn hình
    print(row_text)
