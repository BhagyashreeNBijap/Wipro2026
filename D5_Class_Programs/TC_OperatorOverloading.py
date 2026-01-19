class box1:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value

b1=box1(80)
b2=box1(40)
b3=box1(20)
b4=box1(10)
print(b1+b2)
print(b3+b4)
