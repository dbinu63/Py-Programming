# WAP to find the palindromes in a list of strings using filter & lambda

def main():
    words = ["madam", "india", "happy", "level", "python", "java", "malayalam"]

    b = list(filter(lambda x: x == x[::-1], words))
    print(b)

if __name__ == "__main__":
    main()