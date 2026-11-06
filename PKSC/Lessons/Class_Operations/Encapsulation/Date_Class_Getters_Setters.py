class My_Date:
    def __init__(self, d = 1, m = 1, y = 2000):
        self.day = d
        self.month = m
        self.year = y
    def display(self):
        print(f"{self.month}/{self.day}/{self.year}")
    def is_same(self, other: "My_Date") -> bool:
        return True if self.day == other.day and self.month == other.month and self.year == other.year else False

    def get_day(self):
        return self.day
    def get_month(self):
            return self.month
    def get_year(self):
            return self.year

    def set_day(self, d):
            self.day = d
    def set_month(self, m):
            self.month = m
    def set_year(self, y):
            self.year = y


def main():
    p = My_Date(13, 11, 1985)
    q = My_Date(20, 6, 2009)

    if p.is_same(q) == True: 
        print("Dates are the same")
    else: 
        print("Dates are not the same")

    print(f"Day: {p.get_day()}")
    print(f"Month: {p.get_month()}")
    print(f"Year: {p.get_year()}")

    p.set_day(20)
    p.set_month(6)
    p.set_year(2009)

    print(f"Day: {p.get_day()}")
    print(f"Month: {p.get_month()}")
    print(f"Year: {p.get_year()}")

    if p.is_same(q) == True: 
        print("Dates are the same")
    else: 
        print("Dates are not the same")

if __name__ == "__main__":
    main()