def main(): 
    for i in range(0, 5):
        for j in range(0, 5):
            if (i + j) % 2:
                print("_", end = " ")
            else: 
                print("*", end = " ")
        print()

if __name__ == "__main__":
    main()