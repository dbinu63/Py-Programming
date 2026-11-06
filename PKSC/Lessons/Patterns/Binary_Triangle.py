def main():
    mat = []
    row = 5
    col = 5
    ele = 2

    for i in range(row):
        row_list = []
        for j in range(col):
            while ele != 1 and ele != 0:
                ele = int(input("Enter either 1 or 0: "))
            row_list.append(ele)
            ele = 2
        mat.append(row_list)

        for x in row_list:
            print(x, end = " ")
        print()

    print() 
    for x in mat:
        for y in x:
            print(y, end = " ")
        print()
        
    # Check: 
    isTri = True

    for i in range(row):
        for j in range(col):
            if (j >= i and mat[i][j] != 1) or (j < i and mat[i][j] != 0):
                    isTri = False
                    break
        if not isTri: # this break is not needed
            break
    
    if isTri:
        print("You have entered an upper-right triangle of 1s.")
    else: 
        print("You have not entered an upper-right triangle of 1s.")
    


if __name__ == "__main__":
    main()