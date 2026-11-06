class My_Time:
    def __init__(self, h=12, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def display(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

    @property
    def hour(self):
        return self._hour
    @hour.setter
    def hour(self, h):
        self._hour = h

    @property
    def minute(self):
        return self._minute
    @minute.setter
    def minute(self, m):
        self._minute = m

    @property
    def second(self):
        return self._second
    @second.setter
    def second(self, s):
        self._second = s


def main():
    p = My_Time(10, 45, 30)

    print("Original time:")
    p.display()

    print(f"Hour: {p.hour}")
    print(f"Minute: {p.minute}")
    print(f"Second: {p.second}")

    p.hour = 18
    p.minute = 44
    p.second = 25

    print("\nAfter changing the time:")
    print(f"Hour: {p.hour}")
    print(f"Minute: {p.minute}")
    print(f"Second: {p.second}")

    p.display()


if __name__ == "__main__":
    main()