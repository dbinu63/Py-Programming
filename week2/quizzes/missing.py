def main(): 
    fib = [0, 1, 1, 2, 3, 8, 13, 21]

    print("Current list: ")
    for e in fib:
        print(e, end = " ")
    print("\n")

    for e in range(2, len(fib)):
        if fib[e] != fib[e - 1] + fib[e - 2]:
            print(f"Value: {fib[e - 1] + fib[e - 2]}, missing at position: {e}")
            break
    else:
        print("No missing values detected.")

if __name__ == "__main__":
    main()