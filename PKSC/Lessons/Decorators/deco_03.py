def detail(fun):
    def wrap(*args):
        x = int(args[0])
        y = int(args[1])

        print(f"First operand: {x}")
        print(f"Second operand: {y}")

        z = fun(x, y)
        print(f"Result: {z}")
    return wrap

@detail
def add(a, b):
    return a + b

def main():
    add(10, 20)

if __name__ == "__main__":
    main()