'''#Topics: Introduction to OOPs, Understanding Classes & Objects
Create a class Student that:
1. Has attributes name and roll_no
2. Has a method display_details() to print student information
3. Create at least two objects of the class and display their details write code'''

class Student(object):
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display_details(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)

student1=Student("Bhagyashree",31)
student2=Student("Soumya",32)

student1.display_details()
student2.display_details()

