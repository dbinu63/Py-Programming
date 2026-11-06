def square(a):
    b = list(map(lambda n: n * n, a))
    print(b)

def odd_filter(a):
    b = list(filter(lambda n: n % 2 == 1, a))
    print(b)

def main():
    a = [2, 4, 9, 3, 6, 5]
    print(a)

    square(a)
    odd_filter(a)

if __name__ == "__main__":
    main()