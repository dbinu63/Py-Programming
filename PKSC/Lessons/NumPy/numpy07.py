import numpy as np

def main(): 
    a = np.array([
        [5, 2, 9],
        [7, 3, 8]
    ])
    print(a)

    print("Dimenions: ", a.ndim)
    print("Shape: ", a.shape)
    print("Size: ", a.size)
    print("Type: ", a.dtype)
    print("Item Size: ", a.itemsize)

if __name__ == "__main__":
    main()