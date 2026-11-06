class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def show(self):
        print(f"Vehicle: {self.vehicle}")


class Brand(Vehicle):
    def __init__(self, vehicle, brand):
        super().__init__(vehicle)
        self.brand = brand

    def show(self):
        super().show()
        print(f"Brand: {self.brand}")


class Color(Brand):
    def __init__(self, vehicle, brand, color):
        super().__init__(vehicle, brand)
        self.color = color

    def show(self):
        super().show()
        print(f"Color: {self.color}")


class Type(Color):
    def __init__(self, vehicle, brand, color, vehicle_type):
        super().__init__(vehicle, brand, color)
        self.vehicle_type = vehicle_type

    def show(self):
        super().show()
        print(f"Type: {self.vehicle_type}")


class Model(Type):
    def __init__(self, vehicle, brand, color, vehicle_type, model):
        super().__init__(vehicle, brand, color, vehicle_type)
        self.model = model

    def show(self):
        super().show()
        print(f"Model: {self.model}")


class Gear(Model):
    def __init__(self, vehicle, brand, color, vehicle_type, model, gear):
        super().__init__(vehicle, brand, color, vehicle_type, model)
        self.gear = gear

    def show(self):
        super().show()
        print(f"Gears: {self.gear}")


def main():
    p = Gear(
        "Car",
        "Toyota",
        "Red",
        "Sports Car",
        "Supra",
        "4"
    )

    p.show()


if __name__ == "__main__":
    main()