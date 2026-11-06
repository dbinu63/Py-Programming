import numpy as np

def main(): 
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a[0], a[1], a[4], a[-1], a[-2])

    b = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])
    print(b[0, 0], b[0, 1], b[1, 2], b[2, -1], b[1, -2])

if __name__ == "__main__":
    main()