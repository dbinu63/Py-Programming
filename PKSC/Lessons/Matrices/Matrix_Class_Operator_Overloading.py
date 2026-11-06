 
class MyMatrix:
    def __init__(self, *args, name = "NA"):
        self.data = []
        self.name = name.upper()

        i = 1

        if len(args) == 1:
            # check if arg is matrix or series of lists
            if isinstance(args[0], list):
                if isinstance(args[0][0], list):
                    count = len(args[0][0])

                    # ensure all lists in the matrix are the same length
                    while i < len(args[0]):
                        if len(args[0][i]) != count:
                            raise TypeError("Inconsistent matrix dimensions")
                        else:
                            i += 1
                    # append matrix
                    for n in args[0]:
                        self.data.append(n)
            # check if arg is MyMatrix
            elif isinstance(args[0], MyMatrix):
                for n in args[0].data:
                    self.data.append(n)
            else:
                pass
        elif len(args) > 1:
            if isinstance(args[0], list):
                count = len(args[0])
            
                # ensure all lists in the matrix are the same length
                while i < len(args):
                    if len(args[i]) != count:
                        raise TypeError("Inconsistent matrix dimensions")
                    else:
                        i += 1
                # append matrix
                for n in args:
                    self.data.append(n)
        else:
            print(f"Improper data input: {self.name}")

    def disp(self, sep="\n", sep_list=", "):
        if self.data:
            print(f"Data of {self.name}: ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

            for i in range(len(self.data)):
                length = len(self.data[0]) - 1

                for j in range(len(self.data[0])):
                    if length == 0:
                        print(f"{self.data[i][j]}", end="")
                    else:
                        print(f"{self.data[i][j]}", end=sep_list)

                    length -= 1

                print(sep, end="")

            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("\n\n")
        else:
            print(f"Data of {self.name} not available.")
            print("\n\n")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def Find_Row(self, row):
        if self.data:
            if row not in range(len(self.data)):
                raise IndexError("Invalid row index entered")
            return self.data[row]
        print(f"No row data to return for {self.name}")
        return
        
    def Find_Column(self, column):
        result = []

        if self.data:
            if column not in range(len(self.data[0])):
                raise IndexError("Invalid column index entered")
            for row in range(len(self.data)):
                result.append(self.data[row][column])
            return result
        print(f"No column data to return for {self.name}")
        return

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @property
    def Count(self):
        if not self.data:
            return
        
        num = 0
        for i in range(len(self.data)):
            num += len(self.data[i])

        return num
    
    @property
    def Rows(self):
        if self.data:
            return len(self.data)
    
    @property
    def Columns(self):
        if self.data:
            return len(self.data[0])

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __getitem__(self, index):
        result = []

        # make sure index is a tuple of 2 objects
        if not isinstance(index, tuple) or not len(index) == 2:
            raise IndexError("Invalid index entered. Must be 2 valid integers in format: MyMatrix[#, #]")
        else:
            row, column = index

        # retrieving a whole column
        if isinstance(column, slice):
            if row not in range(len(self.data)):
                raise IndexError("Invalid row index entered")
            return self.data[row]

        # retrieving a whole row
        if isinstance(row, slice):
            if column not in range(len(self.data[0])):
                raise IndexError("Invalid column index entered")
            for row in range(len(self.data)):
                result.append(self.data[row][column])
            return result

        # if index does not fall in matrix dimensions/integer
        if row not in range(len(self.data)) or column not in range(len(self.data[row])):
            raise IndexError("Invalid index entered. Must be valid number or ':'")

        
        return self.data[row][column]

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    def __add__(self, other):
        # if 'other' not MyMatrix of equal dimensions
        if not isinstance(other, MyMatrix) or len(other.data) != len(self.data) or len(other.data[0]) != len(self.data[0]):
            # if 'other' not matrix or list of equal dimensions
            if not isinstance(other, list) or len(other) != len(self.data) or not isinstance(other[0], list) or len(other[0]) != len(self.data[0]):
                raise TypeError("A MyMatrix object can only be added to another MyMatrix or a matrix/number of lists of equal dimensions")

        result = []

        # perform matrix addition
        for i in range(self.Rows):
            new_row = []
            for j in range(self.Columns):
                if isinstance(other, MyMatrix):
                    new_row.append(self.data[i][j] + other.data[i][j])
                else:
                    new_row.append(self.data[i][j] + other[i][j])
            result.append(new_row)

        # returning with appropriate name property
        if isinstance(other, MyMatrix):
            return MyMatrix(result, name=f"{self.name} + {other.name}")
        else:
            return MyMatrix(result, name=f"{self.name} + {other}")


    @staticmethod
    def sum(first_matrix, second_matrix):
        return first_matrix + second_matrix

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # NEEDS CHECKING
    def __mul__(self, other):
        # if 'other' not MyMatrix of valid dimensions
        if not isinstance(other, MyMatrix) or len(other.data) != len(self.data[0]):
            # if 'other' not matrix or list of valid dimensions
            if not isinstance(other, list) or len(other) != len(self.data[0]) or not isinstance(other[0], list):
                raise TypeError("A MyMatrix object can only be multiplied by another MyMatrix or a matrix/number of lists of valid dimensions")

        # perform matrix multiplication
        result = []

        if isinstance(other, MyMatrix):
            for i in range(self.Rows):
                new_row = []
                for j in range(other.Columns):
                    value = 0
                    for k in range(other.Rows):
                        value += self.data[i][k] * other.data[k][j]
                    new_row.append(value)
                result.append(new_row)
        else:            
            for i in range(self.Rows):
                new_row = []
                for j in range(len(other[0])):
                    value = 0
                    for k in range(len(other)):
                        value += self.data[i][k] * other[k][j]
                    new_row.append(value)
                result.append(new_row)
                

        # returning with appropriate name property
        if isinstance(other, MyMatrix):
            return MyMatrix(result, name=f"{self.name} * {other.name}")
        else:
            return MyMatrix(result, name=f"{self.name} * {other}")

    @staticmethod
    def product(first_matrix, second_matrix):
        return first_matrix * second_matrix

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():
    p = MyMatrix(name = "p")
    q = MyMatrix([1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], name = "q")
    r = MyMatrix([[9, 8, 7], [6, 5, 4], [3, 2, 1], [0, 9, 8]], name = "r")
    s = MyMatrix(10, name = "s")
    t = MyMatrix([1, 2, 3, 4, 5], name = "t")
    u = MyMatrix(q, name = "u")

    p.disp()
    q.disp()
    r.disp()
    s.disp()
    t.disp()
    u.disp()

    print("Testing Indexing: ")
    print(f"q[0]: {q[0, 1]}")
    print(f"r[0]: {r[:, 1]}")
    print(f"u[0]: {u[0, :]}\n\n")

    print("Testing Count, Row, Column: ")
    print(f"p: Count = {p.Count}, Rows = {p.Rows}, Columns = {p.Columns}")
    print(f"q: Count = {q.Count}, Rows = {q.Rows}, Columns = {q.Columns}")
    print(f"r: Count = {r.Count}, Rows = {r.Rows}, Columns = {r.Columns}")
    print(f"s: Count = {s.Count}, Rows = {s.Rows}, Columns = {s.Columns}")
    print(f"t: Count = {t.Count}, Rows = {t.Rows}, Columns = {t.Columns}")
    print(f"u: Count = {u.Count}, Rows = {u.Rows}, Columns = {u.Columns}\n\n")

    print("Testing Find_Row, Find_Column: ")
    print(f"p[0]: {p.Find_Row(0)}")
    print(f"q[0]: {q.Find_Row(0)}")
    print(f"r[0]: {r.Find_Row(0)}")
    print(f"s[0]: {s.Find_Row(0)}")
    print(f"t[0]: {t.Find_Row(0)}")
    print(f"u[0]: {u.Find_Row(0)}\n\n")

    print(f"p column 0: {p.Find_Column(0)}")
    print(f"q column 0: {q.Find_Column(0)}")
    print(f"r column 0: {r.Find_Column(0)}")
    print(f"s column 0: {s.Find_Column(0)}")
    print(f"t column 0: {t.Find_Column(0)}")
    print(f"u column 0: {u.Find_Column(0)}")

    print("\nTesting __add__ and sum:")

    v = q + u
    v.disp()

    """w = q + 1
    w.disp()"""
    """w = q + [1, 2, 3, 4]
    w.disp()"""
    """w = q + [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    w.disp()"""
    """w = q + [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
    w.disp()"""
    """w = q + r
    w.disp()"""

    w = q + [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
    w.disp()

    x = MyMatrix.sum(q, u)
    x.disp()

    y = MyMatrix.sum(q, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
    y.disp()

    print("\nTesting __mul__ and product:")
    z = q * r
    z.disp()

    """a = q * 1
    a.disp()"""
    """a = q * [1, 2, 3, 4]
    a.disp()"""
    """a = q * [1, 2, 3]
    a.disp()"""
    """a = q * [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
    a.disp()"""

    a = q * [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]]
    a.disp()

    b = MyMatrix.product(q, r)
    b.disp()

    c = MyMatrix.product(q, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]])
    c.disp()

if __name__ == "__main__":
    main()