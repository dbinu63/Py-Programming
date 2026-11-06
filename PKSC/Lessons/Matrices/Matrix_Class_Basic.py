class Matrix:
    def __init__(self, m=3, n=3):
        self.rows = m
        self.cols = n
        self.data = []

    def read(self):
        self.data = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                num = int(input(f"Enter element [{i}][{j}]: "))
                row.append(num)
            self.data.append(row)

    def show(self):
        for row in self.data:
            for num in row:
                print(num, end=" ")
            print()


def main():
    p = Matrix(2, 3)
    p.read()
    p.show()


if __name__ == "__main__":
    main()