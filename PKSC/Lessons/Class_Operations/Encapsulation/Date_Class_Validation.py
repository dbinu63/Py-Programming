class MyDate:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, d = 1, m = 1, y = 2000):
        self.day = d
        self.month = m
        self.year = y

    def disp(self):
        print(f"{self.day}/{self.month}/{self.year}")

    # Day
    def getDay(self):
        return self.day

    def setDay(self, d):
        if 1 <= d <= MyDate.days[self.month - 1]:
            self.day = d
        else:
            print("Invalid day. ")

    # Month
    def getMonth(self):
        return self.month

    def setMonth(self, m):
        if 1 <= m <= 12:
            self.month = m
        else:
            print("Invalid month. ")

    # Year
    def getYear(self):
        return self.year

    def setYear(self, y):
        if y > 0:
            self.year = y
        else:
            print("Invalid year. ")

    # Date
    def getDate(self):
        return MyDate(self.day, self.month, self.year)

    # no need for input validation since the constructors are already taking care of it, and we're passig the obj here
    def setDate(self, dt):
        self.day = dt.day
        self.month = dt.month
        self.year = dt.year

    def is_same(self, dt):
        return  (self.day == dt.day and self.month == dt.month and self.year == dt.year)


def main():
    pass


if __name__ == "__main__":
    main()