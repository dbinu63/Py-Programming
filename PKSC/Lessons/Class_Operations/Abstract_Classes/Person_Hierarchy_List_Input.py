from __future__ import annotations
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, mob):
        self.name = name
        self.mob_no = mob

    @abstractmethod
    def disp(self):
        print(f"Name: {self.name}")
        print(f"Mobile No.: {self.mob_no}")

    @property
    def Name(self):
        return self.name
    @Name.setter
    def Name(self, name):
        self.name = name

    @property
    def MobileNumber(self):
        return self.mob_no
    @MobileNumber.setter
    def MobileNumber(self, number):
        self.mob_no = number


class Student(Person):
    std_counter = 101

    def __init__(self, name, mob, courses, fees):
        super().__init__(name, mob)
        self.courses = courses
        self.fees = fees
        self.std_code = Student.std_counter

        Student.std_counter += 1

    def disp(self):
        print(f"Student: {self.name}, code: {self.std_code}")
        print(f"Mobile No.: {self.mob_no}")
        print(f"Courses: {self.courses}")
        print(f"Fees: {self.fees}")
        print("- "*10)
        print("\n")

    @classmethod
    def count(cls):
        return cls.std_counter - 101

    @staticmethod
    def Compare(p: Student, q: Student):
        return (p.name == q.name and p.mob_no == q.mob_no and p.courses == q.courses and p.fees == q.fees)

    def __eq__(self: Student, other: Student):
        return (self.name == other.name and self.mob_no == other.mob_no and self.courses == other.courses and self.fees == other.fees)

class Employee(Person):
    emp_counter = 101
    
    def __init__(self, name, mob, department, designation, salary):
        super().__init__(name, mob)
        self.department = department
        self.designation = designation
        self.salary = salary
        self.emp_code = Employee.emp_counter
    
        Employee.emp_counter += 1
    
    def disp(self):
        print(f"Employee: {self.name}, code: {self.emp_code}")
        print(f"Mobile No.: {self.mob_no}")
        print(f"Department: {self.department}")
        print(f"Designation: {self.designation}, Salary: {self.salary}")
        print("- "*10)
        print("\n")

    @classmethod
    def count(cls):
        return cls.emp_counter - 101

class Customer(Person):
    cust_counter = 101
    valid_types = ["bronze", "silver", "gold"]
    
    def __init__(self, name, mob, cust_type):
        super().__init__(name, mob)
        self.cust_code = Customer.cust_counter

        if cust_type not in Customer.valid_types:
            raise ValueError("Invalid customer type")
        self.cust_type = cust_type
    
        Customer.cust_counter += 1
    
    def disp(self):
        print(f"Customer: {self.name}, code: {self.cust_code}")
        print(f"Mobile No.: {self.mob_no}")
        print(f"Customer Type: {self.cust_type}")
        print("- "*10)
        print("\n")

    @classmethod
    def count(cls):
        return cls.cust_counter - 101

# - - -

def main():
    s1 = Student(
        "John Smith",
        "555-123-4567",
        ["Python", "Database", "Web Development"],
        2500
    )

    s2 = Student(
        "Jane Doe",
        "555-987-6543",
        ["Java", "Python"],
        2000
    )

    s = [Student("John Smith", "555-123-4567", ["Python", "Database", "Web Development"], 2500), Student("Jane Doe", "555-987-6543", ["Java", "Python"], 2000)]
    s[0].disp()
    s[1].disp()
    print(f"Student Name: {s[0].Name}")

    courses = ["C", "Python"]
    name = input("Enter a name: ")
    mob_no = input("Enter a mobile number: ")
    
    temp = Student(name, mob_no, courses, 2000)

    s.append(temp)

    s[2].disp()

if __name__ == "__main__":
    main()