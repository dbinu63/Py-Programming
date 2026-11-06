class Matrix():
    def __init__(self, *args):
        if (len(args) == 2):
            self.rows = int(args[0])
            self.cols = int(args[1])
            self.data = []

            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(0)
                self.data.append(row)
        
        elif (len(args) == 1 and isinstance(args[0], Matrix)):
            m = args[0]

            self.rows = m.rows
            self.cols = m.cols
            self.data = []

            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(m.data[i][j])
                self.data.append(row)

        elif (len(args) == 1 and isinstance(args[0], list)):
            self.data = args[0]
            self.rows = len(self.data)

            if self.rows > 0:
                self.cols = len(self.data[0])
            else:
                self.cols = 0
            

        else:
            print("You must pass either 1 or 2 arguments.")

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