def only_positive(func):
    def wrap(*args):
        if args[0] < 0 or args[1] < 0:
            print("Cannot use negative numbers. ")
        else:
            c = func(args[0], args[1])
            print(f"Result: {c}")
    return wrap

@only_positive
def mult(a, b):
    return a * b

def main():
    mult(5,6)
    mult(5,-6)

if __name__ == "__main__":
    main()