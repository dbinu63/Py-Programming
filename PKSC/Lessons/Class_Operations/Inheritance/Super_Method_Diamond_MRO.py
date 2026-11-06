class A:
    def __init__(self):
        print("Class A")
class B (A):
    def __init__(self):
        print("Class B")
        super().__init__()
class C (A):
    def __init__(self):
        print("Class C")
        super().__init__()
class D (B, C):
    def __init__(self):
        print("Class D")
        super().__init__()

def main():
    p = A()

    print("\n- - - - - - - - - - - - - - - - \n")

    q = B()

    print("\n- - - - - - - - - - - - - - - - \n")


    r = C()

    print("\n- - - - - - - - - - - - - - - - \n")


    d = D()

    print("\nD's MRO:")
    print(D.mro())

if __name__ == "__main__":
    main()