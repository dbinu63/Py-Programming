matrix, limb = [], [] # cannot initialize both with the same value (matrix, limb = [] - not allowed)
cols = int(input("How many columns would you like to enter: "))
rows = int(input("How many rows would you like to enter: "))

print("Enter the elements you would like in the matrix:")
for x in range(0, rows):
    for y in range(0, cols):
        limb.append(int(input(f"{x}, {y}: ")))
    matrix.append(limb)
    limb = []

print("The matrix is now set as: ")
for x in range(0, rows):
    for y in range(0, cols):
        print(matrix[x][y], end="  ")
    print()