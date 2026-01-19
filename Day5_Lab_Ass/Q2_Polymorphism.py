'''#Topics: Introduction to Polymorphism, Polymorphism on Operators 
1. Create a class Calculator that demonstrates method overriding
2. Create another class AdvancedCalculator that overrides a method from Calculator
3. Implement operator overloading by overloading the + operator to add two objects of a custom class
4. Demonstrate polymorphism using the same method name with different behaviors give correct code '''

# 1. Base class Calculator
class Calculator:
    def calculate(self, a, b):
        print("Calculator calculate (Addition):", a + b)


# 2. Derived class overriding calculate method
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("AdvancedCalculator calculate (Multiplication):", a * b)


# 3. Operator overloading
class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Number(self.number + other.number)

    def __str__(self):
        return str(self.number)


# 4. Polymorphism using same method name
class Operation:
    def execute(self, a, b):
        print("Generic operation")


class Add(Operation):
    def execute(self, a, b):
        print("Add result:", a + b)


class Multiply(Operation):
    def execute(self, a, b):
        print("Multiply result:", a * b)


# Method overriding
calc = Calculator()
calc.calculate(5, 3)

adv_calc = AdvancedCalculator()
adv_calc.calculate(5, 3)


# Operator overloading
num1 = Number(10)
num2 = Number(20)
num3 = num1 + num2
print("Operator overloading result:", num3)


# Polymorphism
operations = [Add(), Multiply()]
for op in operations:
    op.execute(5, 3)
