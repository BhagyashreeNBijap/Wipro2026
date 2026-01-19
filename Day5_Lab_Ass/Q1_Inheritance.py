'''#Topics: Class types, Introduction to Inheritance, Types of Inheritance
1. Create a base class Vehicle with a method start()
2. Create a derived class Car that inherits from Vehicle
3. Add a class variable to track the number of vehicles created
4. Demonstrate single inheritance and multilevel inheritance with appropriate classes'''

class Vehicle:
    vehicle_count = 0
    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle start")

class Car(Vehicle):
    def start(self):
        print("Car started")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

v=Vehicle()
c = Car()
e = ElectricCar()

v.start()
c.start()
e.start()
e.charge()

print("Total vehicles created:", Vehicle.vehicle_count)
