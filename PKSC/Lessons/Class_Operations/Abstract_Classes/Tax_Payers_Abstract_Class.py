from __future__ import annotations
from abc import ABC, abstractmethod


class TaxPayer(ABC):
    def __init__(self, name, tax_id):
        self.tpname = name
        self.taxID = tax_id

    @abstractmethod
    def disp(self):
        print(f"Name: {self.tpname}")
        print(f"Tax ID: {self.taxID}")

    @property
    def name(self):
        return self.tpname

    @name.setter
    def name(self, name):
        self.tpname = name

    @property
    def taxID(self):
        return self.taxID

    @taxID.setter
    def taxID(self, tax_id):
        self.taxID = tax_id


class Individual(TaxPayer):
    ind_counter = 101

    def __init__(self, name, tax_id, income, age):
        super().__init__(name, tax_id)

        self.income = income
        self.age = age
        self.ind_code = Individual.ind_counter

        Individual.ind_counter += 1

    def disp(self):
        print(f"Individual: {self.tpname}, code: {self.ind_code}")
        print(f"Tax ID: {self.taxID}")
        print(f"Income: ${self.income}")
        print(f"Age: {self.age}")
        print(f"Tax Amount: ${self.calculate_tax()}")
        print("-" * 30)
        print()

    def calculate_tax(self):
        if self.income <= 30000:
            return self.income * 0.10
        elif self.income <= 70000:
            return self.income * 0.20
        else:
            return self.income * 0.30

    def is_senior(self):
        return self.age >= 65

    @classmethod
    def count(cls):
        return cls.ind_counter - 101

    @staticmethod
    def compare(p: Individual, q: Individual):
        return (
            p.name == q.name
            and p.tax_id == q.tax_id
            and p.income == q.income
            and p.age == q.age
        )


class Corporate(TaxPayer):
    corp_counter = 201

    def __init__(self, name, tax_id, revenue, employees, corp_type):
        super().__init__(name, tax_id)

        self.revenue = revenue
        self.employees = employees
        self.corp_type = corp_type
        self.corp_code = Corporate.corp_counter

        Corporate.corp_counter += 1

    def disp(self):
        print(f"Corporate: {self.tpname}, code: {self.corp_code}")
        print(f"Tax ID: {self.taxID}")
        print(f"Corporate Type: {self.corp_type}")
        print(f"Revenue: ${self.revenue}")
        print(f"Employees: {self.employees}")
        print(f"Tax Amount: ${self.calculate_tax()}")
        print("-" * 30)
        print()

    def calculate_tax(self):
        return self.revenue * 0.21

    def large_company(self):
        return self.employees >= 500

    @classmethod
    def count(cls):
        return cls.corp_counter - 201

    @staticmethod
    def compare(p: Corporate, q: Corporate):
        return (
            p.name == q.name
            and p.tax_id == q.tax_id
            and p.revenue == q.revenue
            and p.employees == q.employees
            and p.corp_type == q.corp_type
        )


def main():
    i1 = Individual(
        "John Smith",
        "i1001",
        55000,
        35
    )

    i2 = Individual(
        "David Williams",
        "i1002",
        85000,
        68
    )

    c1 = Corporate(
        "Tech Solutions Inc.",
        "c5001",
        500000,
        120,
        "Corporation"
    )

    c2 = Corporate(
        "Green Services LLC",
        "c5002",
        250000,
        35,
        "LLC"
    )

    i1.disp()
    i2.disp()

    print(f"Individual Count: {Individual.count()}")
    print()

    c1.disp()
    c2.disp()

    print(f"Corporate Count: {Corporate.count()}")
    print()

    print(f"Is {i2.name} a senior? {i2.is_senior()}")
    print(f"Is {c1.name} a large company? {c1.large_company()}")
    print()

    print(f"Comparing i1 and i2: {Individual.compare(i1, i2)}")
    print(f"Comparing c1 and c2: {Corporate.compare(c1, c2)}")


if __name__ == "__main__":
    main()