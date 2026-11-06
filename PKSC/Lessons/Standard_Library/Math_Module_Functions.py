import math as m

def main():
    y = []

    x = m.ceil(2.7)
    print(x)

    x = m.floor(2.7) # rounds to -inf
    print(x)

    x = m.trunc(2.7) # rounds to 0
    print(x)

    x = m.sqrt(144)
    print(x)

    x = m.sqrt(93)
    print(x)

    x = m.isqrt(93) # i stands for integer, not imaginary
    print(x)

    # x = m.sqrt(-144), doesn't allow negative numbers
    # print(x)

    x = m.gcd(12, 18)
    print(x)

    x = m.lcm(12,18)
    print(x)

    x = m.pow(2,3) # pow() also exists within math, just returns float
    print(x)

    x = m.factorial(5)
    print(x)

if __name__ == "__main__":
    main()