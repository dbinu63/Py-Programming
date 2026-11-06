import numpy as np

def main(): 
    a = np.eye(5)
    print(a, "\n")

    a = np.empty(5)
    print(a, "\n")

    a = np.array([3.8, 4.9, 6.1, 7.2, 8.3])
    b = a.astype(int)
    print(a)
    print(b, "\n")

if __name__ == "__main__":
    main()