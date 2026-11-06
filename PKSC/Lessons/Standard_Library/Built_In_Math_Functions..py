def main():
    x = min(9, 4, 2, 7)
    print(x)


    x = max(9, 4, 2, 7)
    print(x)

    # x = sum(9, 4, 2, 7), sum() doesn't allow more than 2 args
    # x = sum(9, 4), sum() expects the first arg to be an iterable object and the second to be the starting point
    y = [9, 4, 2, 7]
    print(type(y))
    x = sum(y)
    print(x)

    x = pow(2, 3)
    print(x)

    x = pow(3, 2)
    print(x)

    x = abs(-2.7)
    print(x)

    # all the above are built in operations. You don't need to import the math package to use them

if __name__ == "__main__":
    main()