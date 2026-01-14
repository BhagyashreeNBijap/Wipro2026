#Create a custom iterator class that iterarte over numbers from 1 to n

class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
obj=NumberIterator(4)

for i in obj:
    print(i)


##Q2 Create a Generator function that yields the first N Fibonacci numbers

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for n in fibonacci(6):
    print(n)

#3.Demonstrate the difference between using the iterator and generator by printing values using a for loop

#Iterator
class MyIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


print("using Iterator:")
for value in MyIterator(5):
    print(value)

# Generator
def my_generator(n):
    for i in range(1, n + 1):
        yield i

print("\n using Generator:")
for value in my_generator(5):
    print(value)
