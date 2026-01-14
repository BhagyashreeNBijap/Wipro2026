class PositiveSalary:
    def __get__(self, instance, owner):
        return instance._salary

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance._salary = value


class Employee:
    salary = PositiveSalary()   # descriptor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary     # calls __set__ of descriptor


# Demonstrates the descriptor by creating multiple Employee objects
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)

# Raises a ValueError if a negative salary is assigned
e3 = Employee("Charlie", -30000)
