class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog sound")

class Cat(Animal):
    def sound(self):
        print("Cat sound")

obj=[Dog(),Cat()]

for b in obj:
    b.sound()
