#Topic: Decorators
'''Write a decorator called @execution_time that: 
1. Measures the execution time of a function 
2. Prints the function name and execution time 
3. Apply this decorator to a function that calculates the factorial of a number using recursion'''

import time

def execution_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("Function name:", func.__name__)
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print("Factorial:", result)
