# set default values for all params
class Date:
    def __init__(self, d = 1, m = 1, y = 2000):
        self.day = d
        self.month = m
        self.year = y
    def display(self):
        print(f"{self.month}/{self.day}/{self.year}")

class Time:
    def __init__(self, h = 12, m = 0, s = 0):
        self.hour = h
        self.minute = m
        self.second = s
    def display(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

class Student:
    def __init__(self, name = "John Smith", sid = 0, age = 0):
        self.name = name
        self.student_id = sid
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Age: {self.age}")

def main():
    date1 = Date(7, 8, 2026)
    date1.display()

    print()
    time1 = Time(10, 30, 0)
    time1.display()

    print()
    student1 = Student("John", "S12345", 20)
    student1.display()

if __name__ == "__main__":
    main()