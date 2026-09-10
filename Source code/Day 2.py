# 1. Các phép toán so sánh
a = 3
b = 3
print(a==b)
# True

c = 4
d = 5
print(c==d) # False

c1 = 4
d1 = 5
print(c1!=d1) # True
print(c1 > d1) # False
print(c1 < d1) # True

# 2. Các phép toán logic
x = 5
y = 10

# AND : True khi cả hai điều kiện đều đúng
print(x > 0 and y > 0) # True

# OR : True khi có ít nhất một điều kiện đúng
print(x > 0 or y > 100) # True

# NOT : True khi điều kiện là False
print(not x > 0) # False

# 3. Biểu thức điều kiện
# IF
age = 18
if(age >= 18) :
    print("Đã đủ 18 tuổi")
else:
    print("Chưa đủ 18 tuổi")
# Đã đủ 18 tuổi

# If...elseif...else
grade = 85
if(grade >= 85) :
    print("Xuất sắc")
elif(grade >= 75) :
    print("Giỏi")
elif(grade >= 65) :
    print("Khá")
else:
    print("Trung bình")
# Xuất sắc    

#  Cho người dùng nhập tên, password. Kiểm tra xem có đúng password hay ko.
# Nếu đúng in ra "Đăng nhập thành công", nếu thì mời nhập lại. (pw:12345)

# username = input("Nhập username: ")
# password = input("Nhập password: ")

# if password == "12345":
#     print("Đăng nhập thành công")
# else:
#     password = input("Sai password, vui lòng nhập lại: ")

#     if password == "12345":
#         print("Đăng nhập thành công")
#     else:
#         print("Đăng nhập thất bại")

# 2.2
# spam_score = int(input("Điểm Spam score:"))
spam_score = 4
if spam_score >= 5 :
    print("Thư rác (Spam) - Đã tự động chuyển vào thùng rác")
else:
    print("Thư thường (Inbox) - Hiển thị trong hộp thư đến")


# 4. Vòng lặp:
# 4.1 for
for i in range(10):
    print(i)

# 4.2 while
i = 1
print(i<= 5)
while i <= 5:
    print(i)
    i += 1
print(i<5)
# True
# 1
# 2
# 3
# 4
# 5
# False

# Tính tổng các số  cho đến khi người dùng nhập số âm
total = 0
number = int(input("Nhập số nguyên dương: "))
while number >= 0:
    total += number
    number = int(input("Nhập số nguyên dương: "))
print("Tổng các số là: ", total)

# Break
rs = 0
while True:
    number = int(input("Nhập số nguyên dương: "))
    if number <= 0:
        break
    rs += number
print("Tổng các số là: ", rs)

# 3.1
for i in range (1,5):
    accuracy = float(input("Độ chính xác(accuracy): "))
    if accuracy >= 0.95:
        print("Epoch [epoch] : Mô hình đạt độ chính xác tối ưu" ,accuracy, ". Dừng huân luyện sớm")
        break
    else:
        print("Epoch [epoch]: Độ chính xác", accuracy, " . Tiếp tục huấn luyện")