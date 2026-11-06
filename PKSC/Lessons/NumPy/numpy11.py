import numpy as np

def main(): 
    a = np.array([
        [1, 2],
        [3, 4]
        ])
    print(np.linalg.det(a)) # only works with squares

    randomRange = np.random.default_rng()
    a = randomRange.integers(1, 100, size=5)
    print(a)

    a = randomRange.random(5) # allows floats
    print(a)

if __name__ == "__main__":
    main()