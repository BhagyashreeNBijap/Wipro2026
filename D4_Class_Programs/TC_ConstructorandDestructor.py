class employee:
    def __init__(self,name):
        self.name=name
        print("Constructir is called")

    def __del__(self):
        print("Destructor is called")

e = employee("Bhagya")
