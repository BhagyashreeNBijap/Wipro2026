class Parent:
    def parent1(self):
        print("Parent 1")

class Child1(Parent):
    def child1(self):
        print("Child 1")

class Child2(Parent):
    def child2(self):
        print("Child 2")

c1=Child1()
c2=Child2()
c1.parent1()
c1.child1()
c2.parent1()
c2.child2()
