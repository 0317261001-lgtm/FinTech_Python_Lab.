def main():
    # Nhập tổng hóa đơn X, phần trăm tip Y, và số người N
    X = float(input("Nhập tổng hóa đơn (X đồng): "))
    Y = float(input("Nhập phần trăm tip (Y %): "))
    N = int(input("Nhập số người chia tiền (N): "))

    # Kiểm tra số người hợp lệ
    if N <= 0:
        print("Số người phải lớn hơn 0.")
        return

    # Tính tổng số tiền bao gồm cả tip
    total_amount = X + (X * Y / 100)

    # Tính số tiền mỗi người phải trả và làm tròn đến số nguyên
    per_person = round(total_amount / N)

    # Hiển thị kết quả
    print(f"Số tiền thực tế mỗi người phải trả: {per_person:,} đồng")

if __name__ == "__main__":
    main()
