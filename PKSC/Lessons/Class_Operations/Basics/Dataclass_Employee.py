from dataclasses import dataclass

@dataclass
class Employee:
    name : str
    department : str
    salary : int

    # def __init__(self): ... - no need to add this

def main():
    p = Employee("James", "HR", 150000)
    q = Employee("Micheal", "IT", 250000)

    print(p)
    print(q)

    print(p.name)

if __name__ == "__main__":
    main()