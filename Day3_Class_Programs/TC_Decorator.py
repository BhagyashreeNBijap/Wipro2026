def mydecorator(func):
    def wrapper():
        print("Before Function Call")
        func()
        print("After Function Call")
    return wrapper

@mydecorator
def sayhello():
    print("Hello")
sayhello()
