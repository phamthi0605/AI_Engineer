class Student:
    def __init__(self, name, studentID):
        self.name = name
        self.studentID = studentID

    def greeting(self):
        print(f"Hello, my name is {self.name} and my student ID is {self.studentID}.")

class AIModel:
    def __init__(self, ten_mo_hinh, phien_ban):
        self.ten_mo_hinh = ten_mo_hinh
        self.phien_ban = phien_ban

class ChatbotAI:
    def __init__(self, ten_bot, ngon_ngu):
        self.ten_bot = ten_bot
        self.ngon_ngu = ngon_ngu

    def tra_loi(self, cau_hoi):
        print(f"[{self.ten_bot}], [{self.ngon_ngu}]. Đang xử lý câu hỏi [{cau_hoi}]")

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(f"Hello, my name is {self.name}")

class Teacher(Person):
    def day_hoc(self):
        print(f"{self.name} is teaching.")

    def greeting(self):
        print(f"My name is {self.name}. Currently, I'm a teacher.")

class RobotAI:
    def __init__(self, ten):
        self.ten = ten
    
    def lam_viec(self):
        print(f"Robot {self.ten} đang hoạt động.")
    
class RobotHutBui(RobotAI):
    def lam_viec(self):
        print(f"Robot {self.ten} đang tự động hút bụi nhà cửa.")


# Khởi tạo Object
student1 = Student("Pham Thi Thi", "001")
print(student1.name)  # Output: Pham Thi Thi

 # Method trong lớp
student1.greeting()  # Output: Hello, my name is Pham Thi Thi and my student ID is 001.

# EX1:
agentName = AIModel("ChatGPT", "4.0")
print(agentName.ten_mo_hinh, agentName.phien_ban)  # Output: ChatGPT 4.0

# EX2:
bot1 = ChatbotAI("VirtualAssistant", "Tiếng Việt")
bot1.tra_loi("Thời tiết hôm nay thế nào?")
# [VirtualAssistant], [Tiếng Việt]. Đang xử lý câu hỏi [Thời tiết hôm nay thế nào?]

# Kế thừa
teacher = Teacher("John")
teacher.day_hoc() # Output: John is teaching.
teacher.greeting()  # Output: Hello, my name is John

# Method ghi đè : lớp con có thể ghi đè method ở class cha
teacher.greeting() # My name is John. Currently, I'm a teacher

# EX4:
robot = RobotHutBui("Xiaomi Bot")
robot.lam_viec()
# Robot Xiaomi Bot đang tự động hút bụi nhà cửa.

