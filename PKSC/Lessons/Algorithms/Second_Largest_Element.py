def main():
    list_a = []

    elements = int(input("How many elements would you like to sort: "))
    print("Enter the elements: ")
    for e in range(0, elements):
        list_a.append(int(input(f"{e + 1}: ")))

    sec = big = 0

    for e in list_a:
        if e > big:
            sec = big
            big = e
        elif e > sec and e != big:
            sec = e
    
    print(f"The second largest element in the list is: {sec}")

if __name__ == "__main__":
    main()