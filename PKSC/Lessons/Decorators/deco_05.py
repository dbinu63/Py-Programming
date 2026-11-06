def round(func):
    def wrap(*args):
        c = int(func(args[0], args[1]) + 0.5)
        return c
    return wrap

@round
def divy(a, b):
    return a / b

def main():
    print(divy(5,3))

if __name__ == "__main__":
    main()