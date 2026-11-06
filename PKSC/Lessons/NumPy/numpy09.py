import numpy as np

def main(): 
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(a)

    a = np.array(a)
    print(a)

    b = a.reshape(3, 4)
    print(b)

    b = a.reshape(4, 3)
    print(b)

    a = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    b = a.flatten()
    print(b)

if __name__ == "__main__":
    main()