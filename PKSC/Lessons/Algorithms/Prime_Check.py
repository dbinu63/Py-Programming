def is_prime(uinput):
    for i in range(2, uinput // 2 + 1):
        if uinput % i == 0:
            return False
    else:
        return True

def main(): 
    x = int(input("Enter an integer: "))

    if is_prime(x):
        print(f"{x} is prime. ")
    else:
        print(f"{x} is not prime. ")

if __name__ == "__main__":
    main()