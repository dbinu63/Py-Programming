class Walker:
    def move(self):
        return "Walking"

class Flyer:
    def move(self):
        return "Walking"

class Bird(Walker, Flyer):
    pass

# - - -

def main():
    b = Bird()
    print(b.move())

    print("\n", Bird.__mro__) # displays pathing compiler takes when accessing methods of the Bird and parent classes
    # print("\n", Bird.__mro__)

if __name__ == "__main__":
    main()