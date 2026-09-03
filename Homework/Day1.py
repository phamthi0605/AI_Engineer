# Bài 1.2
# Bài tập 1.2: AI đánh giá hiệu suất Chatbot
# •	Bối cảnh: Bạn lập trình cho một hệ thống đánh giá chatbot tự động chăm sóc khách hàng sau một ngày hoạt động.
# •	Yêu cầu:
# 1.	Dùng lệnh input() yêu cầu người dùng nhập Tổng số câu hỏi mà khách hàng đã gửi trong ngày (ép kiểu số nguyên int).
# 2.	Yêu cầu nhập Số câu trả lời chưa chính xác của chatbot (ép kiểu số nguyên int).
# •	Các phép tính cần làm:
# o	Phép trừ (-): Tính Số câu trả lời đúng = Tổng số câu hỏi − Số câu trả lời chưa chính xác.
# o	Phép chia (/) và nhân (*): Tính Tỷ lệ chính xác (Accuracy) theo % = (Số câu trả lời đúng / Tổng số câu hỏi) * 100.
# •	Đầu ra mong muốn: Sử dụng print() để in ra kết quả báo cáo của chatbot: "Báo cáo hiệu suất: Chatbot đã trả lời đúng [Số câu đúng] câu hỏi. Đạt tỷ lệ chính xác [Tỷ lệ %]%."

total_Question = int(input("Tổng số câu hỏi: "))
incorrect_Answer = int(input("Số câu trả lời chưa chính xác: "))

correct_Answer = total_Question - incorrect_Answer
accuracy = (correct_Answer / total_Question) * 100
print(f"Báo cáo hiệu suất: Chatbot đã trả lời đúng {correct_Answer} câu hỏi. Đạt tỷ lệ chính xác {accuracy}%.")

# Tổng số câu hỏi: 20
# Số câu trả lời chưa chính xác: 10
# Báo cáo hiệu suất: Chatbot đã trả lời đúng 10 câu hỏi. Đạt tỷ lệ chính xác 50.0%.