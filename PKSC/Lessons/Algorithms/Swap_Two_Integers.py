def main(): 
    x = int(input("Enter an integer: "))
    y = int(input("Enter an integer: "))

    print(f"Int 1: {x} ")
    print(f"Int 2: {y} ")

    x, y = y, x

    print()
    print(f"Int 1: {x} ")
    print(f"Int 2: {y} ")

if __name__ == "__main__":
    main()