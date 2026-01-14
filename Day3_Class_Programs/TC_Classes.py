class student:
    name="Ravi"
    age=25

s1=student()
print(s1.name)
print(s1.age)

class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=employee("Leena",30)
print(e1.name)
print(e1.age)

#or
print(e1.name,e1.age)
