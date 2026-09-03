# Giới thiệu Python và cấu trúc chương trình
print("Hello world")

print("Thi, 27")

# Biến và kiểu dữ liệu
x = 10 # kiểu dữ liệu int (số nguyên) cho biến x
pi = 3.14 # kiểu dữ liệu float (số thực) cho biến pi
name = "Alice" # kiểu string cho biến name
id_student = True # kiểu dữ liệu boolean (True hoặc False) cho biến id_student

#  Tính diện tích hình chữ nhật

a = 3
b = 4
area = a * b
print("Diện tích hình chữ nhật là:",area)

chu_vi = (a+b)*2
print("Chu vi hình chữ là:", chu_vi)

# Tính diện tích hình tròn
r = 5
pi = 3.14
area_ht = pi * r * r
print("Diện tích hình tròn", area_ht)

# Nhập xuất dữ liệu
name = input("Nhập tên của bạn:")
age = int(input("Nhập tuổi: "))
print("Xin chào ", name, "bạn đã", age, "tuổi")

# Tính diện tích hcn (chiều dài, chiều rộng là số thực)
dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
area_hcn = dai * rong
print("Diện tích hcn là: ", area_hcn)

# Bài tập: 
name_AI = input("Nhập tên của trợ lý AI: ")
version = float(input("Nhập phiên bản của trợ lý AI:"))
print(f"Xin chào tôi là trợ lý ảo AI của {name_AI}, phiên bản {version}. Rất vui được hỗ trợ bạn!")


# Bài 1.1
sl_CPU = int(input("Số lượng GPU cần thuê: "))
don_gia = float(input("Đơn giá thuê mỗi GPU/giờ: "))
so_gio = float(input("Nhập số giờ dự kiến huấn luyện: "))
so_tienToiDa = float(input("Số tiền ngân sách tối đa:" ))

tong_chiPhiDuKien = sl_CPU * don_gia * so_gio
so_tienConLai = so_tienToiDa - tong_chiPhiDuKien
so_tienPhongBanPhaiTra = tong_chiPhiDuKien /3

print("Tổng chi phí dự kiến:", tong_chiPhiDuKien)
print("Số tiền còn lại:", so_tienConLai)
print("Số tiền phải trả cho phòng ban: ", so_tienPhongBanPhaiTra)

# Số lượng GPU cần thuê: 12
# Đơn giá thuê mỗi GPU/giờ: 1230
# Nhập số giờ dự kiến huấn luyện: 10
# Số tiền ngân sách tối đa:1000
# Tổng chi phí dự kiến: 147600.0
# Số tiền còn lại: -146600.0
# Số tiền phải trả cho phòng ban:  49200.0

# Bài 1.2
total_Question = int(input("Tổng số câu hỏi: "))
incorrect_Answer = int(input("Số câu trả lời chưa đúng: "))

# correct_Answer = total_Question - incorrect_Answer
# accurracy = correct_Answer / total_Question * 10