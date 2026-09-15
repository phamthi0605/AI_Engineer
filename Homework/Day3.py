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

# Ex3:
words = ["xin chào", "spam", "học tập", "cấm", "python"]
for i in range(len(words)):
    if words[i] == "spam" or words[i] == "cấm":
        print(f"Cảnh báo: Phát hiện từ vi phạm '[{words[i]}]'!")

# Ex4: 
response_time = [0.5, 2.3, 0.8, 3.1, 1.2]
for i in range(len(response_time)):
    if response_time[i] > 2:
        print(f"Thời gian [{response_time[i]}]s - Phản hồi chậm")
    else:
        print(f"Thời gian [{response_time[i]}]s - Phản hồi nhanh")

# Ex5: 
distances = [12, 5, 15, 8, 11, 3]
for i in range(len(distances)):
    if distances[i] < 10 :
        print(f"NGUY HIỂM: Vật cản ở khoảng cách [{distances[i]}]m - Yêu cầu giảm tốc!")