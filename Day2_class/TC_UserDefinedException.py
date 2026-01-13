class MyError(Exception):
    pass
#raise MyError("This is a user defined Exception")

class invalidage(Exception):
    pass



try:
    age=int(input("Enter your age"))
    if age<18:
        raise invalidage("Age must be 18 or above")
    else:
        print("eligible to vote")
except invalidage as e:
    print("Error:",e)
