def is_prime(func):
    def wrapper(*args):
        num = int(args[0])
        for n in range(2, num // 2 + 1):
            if num % n == 0:
                print("The number is not prime. ")
                return func(num)
        else:
            print(f"The number {num} is prime. ")
    return wrapper

@is_prime
def is_perf(num):
    y = 0
    for x in range(1, num // 2 + 1):
        if num % x == 0:
            y += x
        x += 1
    
    if y == num:
        return True
    else: 
        return False

def main():
    num = input("Enter a positive integer. ")
    print("Perfect") if is_prime(num) else print("Not perfect")

if __name__ == "__main__":
    main()