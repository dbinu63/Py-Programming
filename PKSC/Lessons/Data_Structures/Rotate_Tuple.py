def rotate_tuple(tup):
    first = tup[0]
    rest = tup[1:]

    new_tup = rest + (first,)
    return new_tup


def main():
    vals = (1, 2, 3, 4, 5, 6, 7)

    rot = rotate_tuple(vals)

    print("Original:", vals)
    print("Rotated :", rot)


if __name__ == "__main__":
    main()

'''
def rotate(t):
    a = list(t)
    temp = a[0]
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = temp

def main():
    t = (2, 5, 8, 3, 4, 6, 5)
    print(t)
    t = rotate(t)
    print(t)

if __name__ == "__main__":
    main()
'''