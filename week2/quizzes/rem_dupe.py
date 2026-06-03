def main(): 
    unfil = [2, 9, 5, 3, 6, 4, 5, 3, 5, 8]
    fil = []

    for e in unfil:
        if e not in fil:
            fil.append(e)

    for e in fil:
        print(e, end = " ")

if __name__ == "__main__":
    main()