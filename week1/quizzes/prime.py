def main(): 
    x = int(input("Enter an integer: "))

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            print(f"{x} is not prime")
            break
    else:
        print(f"{x} is prime")

if __name__ == "__main__":
    main()