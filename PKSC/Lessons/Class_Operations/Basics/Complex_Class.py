class Complex:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imaginary = i
    def disp(self):
        print(f"{self.real} + i{self.imaginary}")

def main():
    q = Complex(3.2, 5.9)
    q.disp()

    p = Complex(5, 7)
    p.disp()

if __name__ == "__main__":
    main()