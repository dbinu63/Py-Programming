def main():
    a = [[2, 4, 8, 5], [6, 1, 1, 2]]
    b = [[4, 3, 5], [2, 2, 1], [1, 5, 6], [2, 3, 3]]
    c, temp = [], []
    
    '''
    # matrix formation: 
    a, b = [], []

    row_a = int(input("Enter the number of rows for the first matrix: "))
    col_a = int(input("Enter the number of rows for the first matrix: "))

    c, temp = [], []

    row_b = int(input("Enter the number of rows for the first matrix: "))
    col_b = int(input("Enter the number of rows for the first matrix: "))

    for i in range(row_a):
        row_list = []
        for j in range(col_a):
            ele = int(input("Enter the element you want to append"))
            row_list.append(ele)
        a.append(row_list)

    for i in range(row_b):
        row_list = []
        for j in range(col_b):
            ele = int(input("Enter the element you want to append"))
            row_list.append(ele)
        b.append(row_list)
    '''

    # check if matrix multiplication is possible: 
    same = True if len(a[0]) == len(b) else False

    #matrix multiplication logic: 
    if same:
        for i in range(len(a)):
            for j in range(len(b[0])):
                temp.append(0)
            c.append(temp)

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
                print(c[i][j], end = ' ')
            print()
    else: 
        print("Matrix multiplication is not possible. ")

if __name__ == "__main__":
    main()