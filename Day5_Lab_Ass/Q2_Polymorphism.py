'''#Topics: Introduction to Polymorphism, Polymorphism on Operators 
1. Create a class Calculator that demonstrates method overriding
2. Create another class AdvancedCalculator that overrides a method from Calculator
3. Implement operator overloading by overloading the + operator to add two objects of a custom class
4. Demonstrate polymorphism using the same method name with different behaviors give correct code '''

class Calculator:
    def calculate(self, a, b):
        print("Addition:", a + b)

class AdvanceCalculator(Calculator):
    def calculate(self, a, b):
        print("Multiplication:", a * b)

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

c=Calculator()
ac=AdvanceCalculator()
c.calculate(1,2)
ac.calculate(4,2)

n1=Number(10)
n2=Number(20)
n3=n1 + n2

print("Operator Overloading:",n3.value)
