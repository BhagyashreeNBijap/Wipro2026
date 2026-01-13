data = [1, 2, 3, 4, 5, 6, 2, 4]

#List comprehension to store squares of all numbers
sq_list = [x*x for x in data]
print(sq_list)

#Set comprehension to store unique even numbers
even_set = {x for x in data if x%2==0}
print(even_set)

#3. Dictionary comprehension where the key is the number and value is its cube

cube_dict={x:x**3 for x in data}
print(cube_dict)
