class Student:
    sid = 0 # class var

    def __init__(self, name = "N/A", age = 0):
        self.name = name # instance vars
        self.age = age   # ^
        Student.sid += 1
        self.student_id = Student.sid
    def display(self, last="\n"):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Age: {self.age}", end=last)
    def read(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter student age: "))
        print()

def main():
    p = Student()
    q = Student("David Ruth", 18)

    p.read()

    p.display(last="\n\n")
    q.display()

if __name__ == "__main__":
    main()