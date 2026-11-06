def odd_number(x):
    if x % 2 == 1:
        return x
    else: 
        pass

def main():
    a = [4, 5, 8, 3, 2, 9, 7, 6]
    print(a)

    b = list(filter(odd_number, a))
    print(b)

if __name__ == "__main__":
    main()