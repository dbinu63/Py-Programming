import numpy as np

def main(): 
    a = np.zeros(5) # set as float    
    print(a, "\n")

    a = np.zeros((3, 4))
    print(a, "\n")

    a = np.ones(5)
    print(a, "\n")

    a = np.full(5, 7)
    print(a, "\n")

    a = np.full((3, 4), 3)
    print(a, "\n")

    a = np.arange(1, 11) # has start stop step params like slice
    print(a, "\n")

    a = np.arange(1, 11, 2)
    print(a, "\n")

    a = np.arange(11)
    print(a, "\n")

    a = np.linspace(1, 10, 5)
    print(a)

if __name__ == "__main__":
    main()