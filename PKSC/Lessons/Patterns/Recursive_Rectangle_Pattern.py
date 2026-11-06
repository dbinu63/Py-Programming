def draw(a, b):
    if a + b == 9:
        return()

    a += 1

    if a == 6:
        b += 1
        print()
        draw(0, b)
        return()

    print(f"{a + b} ", end = "")

    draw(a, b)

def main():
    draw(0, 0)

    return()

if __name__ == "__main__":
    main()