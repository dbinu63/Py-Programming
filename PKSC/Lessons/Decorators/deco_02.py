def greet(fun):
    def inner():
        print("Hi")
        fun()
        print("Namaste")
    return inner
    
@greet # python decorator
def say():
    print("Hello")

def main():
    say()

if __name__ == "__main__":
    main()