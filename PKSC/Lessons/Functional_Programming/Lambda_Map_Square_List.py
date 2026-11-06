# WAP to create a list by squaring elements of a source list

def main():
    a = [2, 5, 3, 4, 6, 4]
    print(a)

    b = list(map(lambda x: x * x, a))
    print(b)

if __name__ == "__main__":
    main()

