x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))

match (int(x > y)):
    case 1:
        print(f"The first input, {x}, is larger. ")
    case _:
        print(f"The second input, {y}, is larger. ")

# set all of this up in a function called main, and then use an if __name__ == "__main__" statement