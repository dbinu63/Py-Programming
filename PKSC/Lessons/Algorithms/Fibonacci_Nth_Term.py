def get_febo_num(n):
    a, b = 0, 1
    
    for x in range(n - 1):
        a, b = b, a + b
    
    return(a)
    
    

def main():
    n = int(input("How many numbers would you like to print? "))

    print(f"{get_febo_num(n)} is the {n}th number in the fibonacci sequence. ")

    

if __name__ == "__main__":
    main()