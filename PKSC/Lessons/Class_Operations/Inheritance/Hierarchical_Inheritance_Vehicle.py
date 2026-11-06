class Vehicle:
    def __init__(self, brand, color, fuel, model):
        self.brand = brand
        self.color = color
        self.fuel = fuel
        self.model = model

    def show(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Fuel: {self.fuel}")
        print(f"Model: {self.model}")


class Bike(Vehicle):
    def __init__(self, brand, color, fuel, model, bike_type):
        super().__init__(brand, color, fuel, model)
        self.bike_type = bike_type

    def show(self):
        super().show()
        print(f"Bike Type: {self.bike_type}")


class Car(Vehicle):
    def __init__(self, brand, color, fuel, model, car_type):
        super().__init__(brand, color, fuel, model)
        self.car_type = car_type

    def show(self):
        super().show()
        print(f"Car Type: {self.car_type}")


def main():
    p = Bike("Honda", "Red", "Gas", "CBR", "Motorcycle")
    p.show()

    print()

    q = Car("Toyota", "Blue", "Gas", "Sienna", "Minivan")
    q.show()


if __name__ == "__main__":
    main()