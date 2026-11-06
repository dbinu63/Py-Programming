class My_Date:
    def __init__(self, d=1, m=1, y=2000):
        self.day = d
        self.month = m
        self.year = y

    def display(self):
        print(f"{self.month}/{self.day}/{self.year}")

    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, d):
        self._day = d

    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, m):
        self._month = m

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, y):
        self._year = y


def main():
    p = My_Date(13, 11, 1985)

    print("Original date:")
    p.display()

    print(f"Day: {p.day}")
    print(f"Month: {p.month}")
    print(f"Year: {p.year}")

    p.day = 20
    p.month = 6
    p.year = 2009

    print("\nAfter changing the date:")
    print(f"Day: {p.day}")
    print(f"Month: {p.month}")
    print(f"Year: {p.year}")

    p.display()


if __name__ == "__main__":
    main()