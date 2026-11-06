class Student:
    code = 0

    def __init__(self, name="NA", mob_no="NA"):
        Student.code += 1

        self.scode = Student.code
        self.__sname = name
        self.__mob_no = mob_no
        self.courses = []

    @property
    def name(self):
        return self.__sname
    @name.setter
    def name(self, value):
        self.__sname = value

    @property
    def mob_no(self):
        return self.__mob_no
    @mob_no.setter
    def mob_no(self, value):
        self.__mob_no = value

    def disp(self, show_courses=True):
        print(f"{self.name}'s Info:")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("Student Code:", self.scode)
        print("Student Name:", self.name)
        print("Mobile Number:", self.mob_no)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        if show_courses:
            print("\n")
            print(f"\n{self.name}'s Courses: ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            if self.courses:
                for course in self.courses:
                    print(f"- {course}")
            else:
                print("No courses to display. ")

            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        print("\n\n")


    def get_info(self):
        return {
            "name": self.name,
            "code": self.scode,
            "num": self.mob_no
        }

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False

        return (
            self.name == other.name
            and self.mob_no == other.mob_no
        )

    @classmethod
    def total_students(cls):
        return cls.code

    def add_course(self, course):
        self.courses.append(course)


def main():
    p = Student()
    q = Student("David")
    r = Student("David", "123 456 7890")
    s = Student(mob_no="123 456 7890")

    p.disp()
    print()

    q.disp(show_courses=False)
    print()

    r.add_course("Python")
    r.add_course("Database")
    r.disp()
    print()

    print(f"R info: {r.get_info()}")

    q.name = "John"
    q.mob_no = "555 555 5555"

    print()
    q.disp(show_courses=False)

    print()
    print("q == r:", q == r)

    print()
    print(f"Total Number of Students: {Student.total_students()}")


if __name__ == "__main__":
    main()

    # finish show sales and show invoice, fix __str__ in myList