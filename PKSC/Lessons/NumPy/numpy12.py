import numpy as np

def main(): 
    a = [2, 5, 12, 0, 4, 13]
    print(np.sort(a))

    a = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60, 10, 70, 10, 80, 10, 90, 10, 100]
    print(np.unique(a))

    values, counts = np.unique(a, return_counts=True)
    print("Values: ", values, "Counts: ", counts)

if __name__ == "__main__":
    main()