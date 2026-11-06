from abc import ABC, abstractmethod


class TaxPayer(ABC):
    def __init__(self, name, tax_id, revenue):
        self.tname = name
        self.taxID = tax_id
        self.revenue = revenue

    @abstractmethod
    def disp(self):
        print(f"Name: {self.tname}")
        print(f"Tax ID: {self.tax_id}")

    @property
    def name(self):
        return self.tname

    @name.setter
    def name(self, name):
        self.tname = name

    @property
    def taxID(self):
        return self.tax_id

    @taxID.setter
    def taxID(self, tax_id):
        self.tax_id = tax_id


class Individual(TaxPayer):

    def __init__(self, name, tax_id, income):
        super().__init__(name, tax_id, income)

    def disp(self):
        print(f"Individual: {self.tname}")
        print(f"Tax ID: {self.tax_id}")
        print(f"Income: ${self.revenue}")
        print(f"Tax Amount: ${self.calculate_tax()}")
        print("-" * 30)
        print()

    def calculate_tax(self):
        return self.revenue * 0.2


class Corporate(TaxPayer):

    def __init__(self, name, tax_id, profit, corp_type):
        super().__init__(name, tax_id, profit)

        self.corp_type = corp_type

    def disp(self):
        print(f"Corporate: {self.tname}")
        print(f"Tax ID: {self.tax_id}")
        print(f"Corporate Type: {self.corp_type}")
        print(f"Profit: ${self.revenue}")
        print(f"Tax Amount: ${self.calculate_tax()}")
        print("-" * 30)
        print()

    def calculate_tax(self):
        return self.revenue * 0.3


def main():
    i1 = Individual(
        "John Smith",
        "i1001",
        55000
    )

    i2 = Individual(
        "David Williams",
        "i1002",
        85000
    )

    c1 = Corporate(
        "Tech Solutions Inc.",
        "c5001",
        500000,
        "Corporation"
    )

    c2 = Corporate(
        "Green Services LLC",
        "c5002",
        250000,
        "LLC"
    )

    i1.disp()
    i2.disp()

    c1.disp()
    c2.disp()


if __name__ == "__main__":
    main()