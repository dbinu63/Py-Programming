def fun(num, *args, **kwargs):
    print(f"Nums: {num}\n")

    print("Args: ")
    i = 1
    for a in args:
        print(i, ":", a)
        i += 1
    print()
    
    print("Kwargs: ")
    i = 1
    for b, c in kwargs.items():
        print(f"{i}: {b}, {c}")
        i += 1

def main():
    fun(1, 2, 3, 4, 5, a = 6, b = 7, c = 8, d = 9, e = 10)

if __name__ == "__main__":
    main()