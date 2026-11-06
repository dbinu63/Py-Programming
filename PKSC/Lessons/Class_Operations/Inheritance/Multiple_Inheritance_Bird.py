class Walker():
    def __init__(self):
        pass
    def move(self):
        return "walking"
class Flyer:
    def __init__(self):
        pass
    def move(self):
        return "flying"
class Bird(Walker, Flyer):
    pass

def main():
    p = Bird()

    print(p.move())

if __name__ == "__main__":
    main()