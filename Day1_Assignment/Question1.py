from functools import reduce

for i in range(1,21):
    print(i)


num=range(1,21)
even_num=list(filter(lambda x:x%2==0,num))
print(even_num)


#3. Uses map() with a lambda to square the filtered numbers
squared_filterednum=list(map(lambda x:x**2,even_num))
print(squared_filterednum)


#4. uses reduce() to calcualte the sum of squared even numbers
sum_of_squares=reduce(lambda x, y: x + y, squared_filterednum)
print(sum_of_squares)


#5. uses enumerate() to print the index and value of the final result list
for index, value in enumerate(squared_filterednum):
    print(index, value)
