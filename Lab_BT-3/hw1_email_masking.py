# 1. Yêu cầu nhập một địa chỉ email từ bàn phím
email = input("Nhập địa chỉ email của khách hàng: ")

# 2. Dùng split("@") để tách phần tên đăng nhập và phần tên miền (domain)
username, domain = email.split("@")

# 3. Trích xuất 3 ký tự đầu tiên của tên đăng nhập (dùng Slicing [0:3])
first_three_chars = username[0:3]

# 4. Ghép 3 ký tự đầu + chuỗi "***@" + tên miền
masked_email = first_three_chars + "***@" + domain

# In kết quả ra màn hình
print("Email sau khi bảo mật:", masked_email)
