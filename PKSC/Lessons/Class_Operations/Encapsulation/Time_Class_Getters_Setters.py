class My_Time:
    def __init__(self, h=12, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def display(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

    def get_hour(self):
        return self.hour
    def get_minute(self):
        return self.minute
    def get_second(self):
        return self.second

    def set_hour(self, h):
        self.hour = h
    def set_minute(self, m):
        self.minute = m
    def set_second(self, s):
        self.second = s


def main():
    p = My_Time(10, 45, 30)
    q = My_Time(5, 20, 40)

    print("Times:")
    p.display()
    q.display()

    print()
    print(f"Hour: {p.get_hour()}\nMinute: {p.get_minute()}\nSecond: {p.get_second()}\n")

    p.set_hour(18)
    p.set_minute(44)
    p.set_second(25)

    print(f"Hour: {p.get_hour()}\nMinute: {p.get_minute()}\nSecond: {p.get_second()}\n")

    p.display(last=" + ")
    q.display(last=": \n")
    p.add_times(q)
    p.display()


    r = My_Time(2, 35, 50)
    w = My_Time(4, 40, 30)

    r.display(last=" + ")
    w.display(last=": \n")
    r.add_times(w)
    r.display()


if __name__ == "__main__":
    main()
