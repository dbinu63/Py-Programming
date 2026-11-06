# WAP to create a list of sorted and unique elements from a source list, where the target elements are the square of the source if they are even - otherwise, double, using lambda. 
# Ex: source = [4, 3, 9, 2, 5, 2, 6, 2, 3] -> tar = [2, 3, 5, 6, 9] -> [4, 6, 10, 36, 18]

def main():
    a = [4, 3, 9, 2, 5, 2, 6, 2, 3]
    b = list(set(a))
    b.sort()

    b = list(map(lambda x: x * x if x % 2 == 0 else x * 2, b))
    print(a, "\n", b)

if __name__ == "__main__":
    main()