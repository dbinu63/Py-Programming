def main(): 
    x = int(input("Enter an integer: "))
    fact = 1

    for i in range(2, x + 1):
        fact *= i

    print()
    print(f"{x}!: {fact} ")

if __name__ == "__main__":
    main()