def main():
    list_a = []

    elements = int(input("How many elements would you like to sort: "))
    print("Enter the elements: ")
    for e in range(0, elements):
        list_a.append(int(input(f"{e + 1}: ")))

    print("Current list: ")
    for e in range(0, elements):
        print(list_a[e], end = " ")

if __name__ == "__main__":
    main()