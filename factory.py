"""
se utiliza para crear objetos complejos de manera eficiente y
flexible. En este patrón, una fábrica se encarga de crear
objetos de una clase específica, lo que permite una mayor
modularidad y reutilización del código
"""


# Clase base para objetos creados por la fábrica
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        raise NotImplementedError()


# Clase para crear objetos Car
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print(f"{self.brand} car started.")


# Clase para crear objetos Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print(f"{self.brand} motorcycle started.")


# Fábrica de vehículos
class VehicleFactory:
    def create_vehicle(self, vehicle_type, brand):
        if vehicle_type == "car":
            return Car(brand)
        elif vehicle_type == "motorcycle":
            return Motorcycle(brand)
        else:
            raise ValueError("Invalid vehicle type.")


# Uso del patrón de Fábrica
vehicle_factory = VehicleFactory()

car = vehicle_factory.create_vehicle("car", "Toyota")
car.start()
# Output: Toyota car started.

motorcycle = vehicle_factory.create_vehicle("motorcycle", "Honda")
motorcycle.start()
# Output: Honda motorcycle started.
