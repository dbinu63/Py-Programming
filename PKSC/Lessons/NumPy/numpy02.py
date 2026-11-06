import numpy as np

def main(): 
    a = np.array([1, 2, 3, 4])
    print(type(a), "\n")

    a = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80]
    ])
    print(a, "\n")

    b = np.array([
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [0, 1, 2]]
    ])
    print(b)

if __name__ == "__main__":
    main()