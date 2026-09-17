def sum(a,b):
    return a+b

def greeting(name):
    print("Hello, " + name)

# viết 1 hàm tính area hình chữ nhật
def area_rectangle(length, width):
    return length * width

# tính tổng, hiệu, tích, thương
def cal(a, b):
    return a + b, a - b, a*b, a/b


total = sum(10,20)
print(total)

greeting("Thi")

area_hcn = area_rectangle(5,3)
print("Area of rectangle is:", area_hcn)


a = 3
b = 4
print(cal(a,b)) #(7, -1, 12, 0.75)


# Biến cục bộ và biến toàn cục
def my_function():
    local_var = 5 # Biến cục bộ
    print(f"Local var: {local_var}")

y = 5
def glo_variable():
    print(f"Global var: {y}") # Biến toàn cục

def chang_var():
    global y # Biến toàn cục
    y = 10 # Gán giá trị mới
    print(f"Changed global var: {y}")

def chao_user(ten, vaitro = "User"):
    print(f"Xin chào,{ten}! Bạn đang đăng nhập với vai trò {vaitro}. Trợ lý AI đã sẵn sàng")

def tinh_accuracy(so_cau_dung, tong_so_cau):
    accuary = (so_cau_dung /tong_so_cau) * 100
    return accuary

def kiem_tra_an_toan(khoang_cach):
    if khoang_cach < 10:
        return "CẢNH BÁO: Dừng xe khẩn cấp!"
    else:
        return "AN TOÀN: Tiếp tục di chuyển."

# Ex1:
chao_user("Nguyễn Văn A","Admin") 
chao_user("Pham Thi Thi")
# Xin chào,Nguyễn Văn A! Bạn đang đăng nhập với vai trò Admin. Trợ lý AI đã sẵn sàng
# Xin chào,Pham Thi Thi! Bạn đang đăng nhập với vai trò User. Trợ lý AI đã sẵn sàng

# Ex2:
so_cau_dung = tinh_accuracy(85, 100)
print(so_cau_dung)
# 85.0

# Ex3:
print(kiem_tra_an_toan(7)) 
# CẢNH BÁO: Dừng xe khẩn cấp!

my_function()
glo_variable()
chang_var()

# Hàm Lambda : là hàm ko cần khai báo def
# Hàm bình phương
binh_phuong = lambda x : x**2

print(binh_phuong(4))









