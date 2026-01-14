class mydescriptor:
    def __get__(self, obj, owner):
        print("Getting Value")
        return obj._x
    def __set__(self, obj, value):
        print("Setting the Value")
        obj._x=value

class Test:
    x=mydescriptor
t=Test()
t.x=10
print(t.x)
