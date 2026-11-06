import numpy as np

def main(): 
    a = np.array([10, 20, 30, 40, 50])
    print("Sum: ", np.sum(a))
    print("Mean: ", np.mean(a))
    print("Media: ", np.median(a))
    print("Minimum: ", a.min())
    print("Maximum: ", a.max())
    print("Standard Deviation: ", np.std(a))

    print(np.sqrt(144))
    print(np.square(5))
    print(np.abs(-13))
    print(np.round(4.3))
    print(np.round(4.8))
    print(np.floor(4.3))
    print(np.ceil(4.3))

    print(np.cumsum([1, 2, 3, 4, 5]))
    print(np.cumprod([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()