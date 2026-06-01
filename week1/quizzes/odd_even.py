def main(): 
    x = int(input("Enter an integer: "))

    match (x % 2):
        case 1:
            print(f"{x} is an odd number")
        case _:
            print(f"{x} is an even number")

if __name__ == "__main__":
    main()