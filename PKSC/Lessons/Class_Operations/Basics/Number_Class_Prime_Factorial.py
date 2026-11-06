class Num:
    def __init__(self, n):
        self.data = n
    def show(self):
        print(f"Number is: {self.data}")
    def is_prime(self):
        for i in range(2, (self.data // 2) + 1):
            if self.data % i == 0:
                return False
        else:
            return True
    def calc_fact(self):
        fact = 1
        for n in range(2, self.data + 1):
            fact *= n
        return fact

def main():
    p = Num(8)
    p.show()

    if p.is_prime():
        print(f"{p.data} is prime")
    else:
        print(f"{p.data} is not prime")

    print(f"Factorial is {p.calc_fact()}")

if __name__ == "__main__":
    main()