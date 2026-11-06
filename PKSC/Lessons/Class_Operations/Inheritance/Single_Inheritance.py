class First:
    def __init__(self, a):
        self.a = a

    def disp(self):
        print(f"Base: {self.a}")

class Second(First):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b;

    def show(self):
        print(f"Base: {self.a}, Derived: {self.b}")

def main():
    p = First(10)
    p.disp()
    # p.show()

    q = Second(100, 200)
    q.disp()
    q.show()

if __name__ == "__main__":
    main()