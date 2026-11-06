class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine: 
        def __init__(self): 
            self.status = "OFF"

        def start(self):
            self.status = "ON"
            print("The engine has been started")

        def stop(self):
            self.status = "OFF"
            print("The engine has been turned off")

    def drive(self): 
        if self.engine.status == "ON":
            print("Driving car...")
        else:
            print("You must start the car before driving")

def main():
    p = Car("Toyota", "Rav4")

    p.engine.start()

    p.drive()

if __name__ == "__main__":
    main()