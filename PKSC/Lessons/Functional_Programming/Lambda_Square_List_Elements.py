# WAP to display square of all elements in a list through a user function with the help of a lambd afunction

def func(lst):
    for n in lst:
        print(f"Number is: {n}. ")
        # sqr = lambda x: x * x
        # print(f"Square is {sqr(n)}. ")
        print(f"Square is {(lambda x: x * x)(n)}")


def main():
    a = [2, 5, 3, 4, 6, 4]
    print(a)

    func(a)

if __name__ == "__main__":
    main()

