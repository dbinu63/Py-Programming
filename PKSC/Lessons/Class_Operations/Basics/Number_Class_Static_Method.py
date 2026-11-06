class Number:
    def __init__(self, n = 0):
        self.data = n
    def show(self):
        print(f"Number is {self.data}")
    def add(self, m):
        if isinstance(m, Number):
            self.data += m.data
        else:
            self.data += m
    @staticmethod # notice that self and cls cannot be used in static method, class ame is used to call
    def addTwo(m, n):
        return m + n


def main():
    p = Number(10)
    q = Number(50)

    p.show()
    p.add(20)
    p.show()

    q.add(p)
    q.show()

    print(f"Sum of 5 and 7 is: {Number.addTwo(5, 7)}")

if __name__ == "__main__":
    main()