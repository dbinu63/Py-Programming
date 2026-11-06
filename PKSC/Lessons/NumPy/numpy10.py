import numpy as np

def main(): 
    a = np.array([
        [10, 20, 30], 
        [40, 50, 60]])
    print(a.T)
    print(a)

    b = a.transpose()
    print(b)

    a = np.array([1, 2, 3, 4])
    b = np.array([4, 5, 6])
    c = np.concatenate((a, b))
    print(c)

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = np.concatenate((a, b), axis=0) # axis 0 for row
    print(c)

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = np.concatenate((a, b), axis=1) # axis 1 for column
    print(c)

if __name__ == "__main__":
    main()