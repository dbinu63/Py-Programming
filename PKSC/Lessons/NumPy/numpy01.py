import numpy as np

def main(): 
    a = [5, 10, 15, 20, 25]
    b = []

    for n in a:
        b.append(n * 2)

    print("Source list:")
    print(a, "\n")

    print("Target list:")
    print(b)

    # - - - - - - -
    print("\n")

    x = np.array(a)
    y = x * 2

    print("Source list:")
    print(x, "\n")

    print("Target list:")
    print(y)

if __name__ == "__main__":
    main()