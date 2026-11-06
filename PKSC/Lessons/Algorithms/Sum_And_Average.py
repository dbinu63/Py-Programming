def sum_avg(list):
    sum, avg = 0, 0

    for e in list:
        sum += e
    # or sum(list)
    
    avg = sum / len(list)

    return(sum, avg)


def main():
    list = [4, 3, 4.5, 15, 2, 8.7, 7]

    sum, avg = sum_avg(list)

    print(f"From list {list}, the sum is {sum} and the average is {avg:.2f}. ")

if __name__ == "__main__":
    main()