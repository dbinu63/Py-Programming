class Complex: 
    def __init__(self, r: int = 0, i: int = 0) -> None:
        self.__rval: int = r
        self.__ival: int = i

    def display(self) -> None:
        print(f"The complex number is: {self.__rval} + {self.__ival}i")

    @property
    def Real(self) -> int:
        return self.__rval

    @property
    def Imaginary(self) -> int:
        return self.__ival

    @Real.setter
    def Real(self, r: int) -> None:
        self.__rval = r

    @Imaginary.setter
    def Imaginary(self, i: int) -> None:
        self.__ival = i

    def add(self, other: "Complex") -> "Complex":
        return Complex(
            self.Real + other.Real,
            self.Imaginary + other.Imaginary
        )

    @staticmethod
    def sum(p: "Complex", q: "Complex") -> "Complex":
        return Complex(
            p.Real + q.Real,
            p.Imaginary + q.Imaginary
        )

    def __add__(self, other: "Complex") -> "Complex":
            return Complex(
                self.Real + other.Real,
                self.Imaginary + other.Imaginary
            )


def main():
    p = Complex(3, 5)
    q = Complex(10, 7)

    r = p.add(q)
    r.display()

    s = Complex.sum(p, r)
    s.display()

    t = p + s
    t.display()


if __name__ == "__main__":
    main()