class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()
    class CPU:
        def process(self):
            print("CPU is now processing...")
    class RAM:
        def save(self):
            print("Contents are saving...")

def main():
    p = Computer()
    p.cpu.process()
    p.ram.save()

if __name__ == "__main__":
    main()