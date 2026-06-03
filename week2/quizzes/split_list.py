def main():
    list_a = [2, 9, 5, 3, 6, 4]

    n = len(list_a) // 2
    if len(list_a) % 2 == 1:
        n += 1

    for e in range(0, n - 1):
        sum = list_a[e] + list_a[e + n]
        list_a[e + n] *= list_a[e]
        list_a[e] = sum

    print("Final list: ")
    for e in list_a:
        print(e, end = " ")
    print("\n")
    
if __name__ == "__main__":
    main()