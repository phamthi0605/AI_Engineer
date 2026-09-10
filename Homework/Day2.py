# 2.2
spam_score = int(input("Điểm Spam score:"))
if spam_score >= 5 :
    print("Thư rác (Spam) - Đã tự động chuyển vào thùng rác")
else:
    print("Thư thường (Inbox) - Hiển thị trong hộp thư đến")

# 2.3
curr_temp = float(input("Nhiệt độ hiện tại của GPU: "))
if curr_temp < 65 :
    print("Trạng thái: GPU hoạt động mát mẻ")
elif curr_temp < 80 :
    print("Trạng thái: GP hơi nóng. Hệ thống tự động tăng tốc độ quạt gió")
else:
    print("Cảnh báo: GPU quá nhiệt! Tự động ngắt tiến trình huấn luyện AI để bảo vệ phần cứng.")


# 3.2
so_san_pham_loi = 0
for i in range(1, 5) :
    diem_chat_luong = int(input("Điểm chất lượng: "))
    if diem_chat_luong < 5:
        print("Sản phẩm lỗi")
        so_san_pham_loi += 1
    print(so_san_pham_loi)


# 3.3
so_lan_thu = 0
while so_lan_thu < 3:
    otp = input("Nhập mã kích hoạt: ")
    so_lan_thu += 1
    if(otp == "Open-AI"):
        print("Kích hoạt trợ lý AI thành công!")
        break
    else:
        print("Mật mã không đúng!")

