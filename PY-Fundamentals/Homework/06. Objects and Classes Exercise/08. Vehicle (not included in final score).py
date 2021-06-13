class Vehicle:
    def __init__(self, type_of_vehicle: str, model_of_vehicle: str, price_of_vehicle: int or float):
        self.type = type_of_vehicle
        self.model = model_of_vehicle
        self.price = price_of_vehicle
        self.owner = None

    def buy(self, money: int, owner: str):
        if money > self.price and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {self.price - money:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)

