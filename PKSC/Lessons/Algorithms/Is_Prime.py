def main(): 
    unfil = [18, 25, 9, 11, 17, 14, 29, 43, 22, 30,]
    fil = []

    for e in unfil:
        for i in range(2, e // 2 + 1):
            if e % i == 0:
                fil.append(0)
                break
        else:
            fil.append(1)

    for e in range(0, len(unfil)):
        print(f"{unfil[e]} - {fil[e]}")

if __name__ == "__main__":
    main()