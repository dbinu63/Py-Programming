class Person:
    def __init__(self, code, name, mobno):
        self.code = code
        self.name = name
        self.mobno = mobno

class Student(Person):
    __next_code = 100

    def __init__(self, name, mob, course, fee):
        Student.__next_code += 1
        sc = Student.__next_code

        super().__init__(sc, name, mob)

        self.course = course
        self.fees = fee

    def display(self):
        print(f"Name: {self.name}")
        print(f"Code: {self.code}")
        print(f"Mob. No.: {self.mobno}")
        print(f"Courses: {self.course}")
        print(f"Fees: {self.fees}")

# - - -

def main():
    david_j = Student("David Johnson", "1246019955", ["math", "python", "java"], 5000)
    david_j.display()

if __name__ == "__main__":
    main()