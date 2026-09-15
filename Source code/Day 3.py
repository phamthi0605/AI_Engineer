# 1. List : có thể chứa nhiều kiểu dữ liệu khác nhau, có thứ tự, có thể thay đổi, cho phép trùng nhau
empty_list = []
list_int = [1, 2, 3]
list_char = ['a', 'b', 'c']

number = [1, 2, 3, 4, 5]
print(number[1])
print(number[-1])
print(number[1:3])

# 1.1 Chức năng của list
# Append : thêm một phần tử vào cuối list
number.append(6)
print(number) #[1, 2, 3, 4, 5, 6]

# Insert: thêm một phần tử vào vị trí bất kì trong list
number.insert(2, 7)
print(number) # [1, 2, 7, 3, 4, 5, 6]

# Remove: xóa một phần tử khỏi list
number.remove(1)
print(number) #[2, 7, 3, 4, 5, 6]

number.pop()
print(number) #[2, 7, 3, 4, 5]

number.clear()
print(number) # []

# Cắt 1 đoạn của list
new_list = [1, 2, 3, 4, 5]
sub_List = new_list[1:3]
print(sub_List) #[2, 3]

# 1.2 Các phương thức của List
# Sort :
listSort = [1, 6, 3, 8, 9, 4]
listSort.sort()
# listSort.sort(reverse=True) # [9, 8, 6, 4, 3, 1]
print(listSort) #[1, 3, 4, 6, 8, 9]

listString = ['a', 'd', 'c', 'b']
listString.sort()
print(listString)  #['a', 'b', 'c', 'd']

# Reverse:
listString.reverse()
print(listString)  #['d', 'c', 'b', 'a']

# Count
listCount = [1, 2, 3, 4, 1]
print(listCount.count(1))  # 2

# Extend:
listCount.extend([5, 6, 7])
print(listCount) #[1, 2, 3, 4, 1, 5, 6, 7]

#  Một số ví dụ với danh sách for
for i in range (len(listCount)) :
    print(listCount[i])

# Cộng tất cả các phần tử trong list
sum = 0
for i in range (len(listCount)) :
    sum += i
print(sum)

#  duyệt toàn bộ danh sách in ra các phần tử nhỏ hơn 40
list_check = [10, 20, 40, 60, 30, 50]
for i in range (len(list_check)) :
    if list_check[i] < 40 :
        print(list_check[i])
# 10
# 20
# 30

# Ex1:
scores = [0.92, 0.45, 0.88, 0.30, 0.75]
for i in range(len(scores)):
    if scores[i] >= 0.7:
        print(f"Vật thể hợp lệ (Độ tin cậy: {scores[i]})")
    else:
         print(f"Nhiễu/ Bỏ qua (Độ tin cậy: {scores[i]})")

# Ex2:
feedbacks = ["Positive", "Negative", "Positive","Negative", "Negative" ]
so_luong_negative = 0
for i in range(len(feedbacks)):
    if feedbacks[i] == "Negative":
        so_luong_negative += 1
print(f"Số feedback tiêu cực:[{so_luong_negative}]")

# 2. Dictionary: ko thể trùng nhau, có thể thay đổi

dict = {
    "name" : "Thi",
    "age" : 27,
    "gender" : "female",
    "address" : "Hà Nội"
}

# in tất cả
for key, value in dict.items():
    print(key, ":", value)

del dict["address"]
print(dict)

# Tính điểm trung bình
sinh_vien = {
    "Toán" : 10,
    "Lý" : 9,
    "Hoá" : 8
}
total  = 0
for key, value in sinh_vien.items():
    total = total + value
avg = total / len(sinh_vien)

print(total)
print(avg)
