students={
    "name": "Bhagya",
    "age": 23,
    "Course": "Python"

}
print(students)


student={

    "name": "Abhi",
    "age": 26,
    "Course": "Java"

}
print(student)
print(student["name"])
print(student.get("age"))

student["Marks"]=85
student["age"]=25
print(student)
print(student["name"])
print(student.get("age"))
student.pop("age")
print(student)
student.popitem()
print(student)

print(student.keys())
print(student.values())


for key in student:
    print(key,student[key])

if "name" in student:
    print("key exists")

employees={

    101:{"name":"leena","salary":2000},
102:{"name":"leena","salary":2000},

}

print(employees[101]["name"])
