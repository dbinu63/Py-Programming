def main(): 
    x = int(input("Enter an integer: "))
    sum = 0

    while (x > 9):
        sum += x % 10
        x //= 10
    sum += x

    print(f"Sum of digits is: {sum}")

if __name__ == "__main__":
    main()