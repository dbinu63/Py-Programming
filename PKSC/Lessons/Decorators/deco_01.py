def greet(fun):
    def inner():
        print("Hi")
        fun()
        print("Namaste")
    return inner

def say():
    print("Hello")

welcome = greet(say)

def main():
    welcome()

if __name__ == "__main__":
    main()