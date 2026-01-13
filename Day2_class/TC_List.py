numbers=[10,20,30,40]
names=["Abhi","Akash","Bhagya"]
mixed = [1, "Python", 3.5, True]
numbers[1] = 100
print(numbers)
print(names)
print(mixed)

for i in numbers:
    print(i)
if 10 in numbers:
    print("Found")
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])

names.reverse()
print(names)
names.append("kalai")
print(names)

names.extend(["pavan","leela"])
print(names)

names.remove("kalai")

print(names)

names.insert(3,"uma")
