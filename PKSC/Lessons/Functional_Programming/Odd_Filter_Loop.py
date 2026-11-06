def odd_filter(lst):
    tar = []
    for x in lst: 
        if x % 2 == 1:
            tar.append(x)
    return tar

def main():
    a = [4, 5, 8, 3, 2, 9, 7, 6]
    print(a)

    b = odd_filter(a)
    print(b)

if __name__ == "__main__":
    main()