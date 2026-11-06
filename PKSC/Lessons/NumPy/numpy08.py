import numpy as np

def main(): 
    a = np.array([10, 20, 30])
    b = np.array([1, 2, 3])

    c = a + b
    print(c) # prints 11, 22, 33
    # +, -, *, **, /, %, all allowed

    c = a ** b
    print(c)

    a = a + 5 # scalar addition
    print(a)

if __name__ == "__main__":
    main()