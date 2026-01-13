num=4
if num%2==0:
    print("Even")
else:
    print("Odd")

marks=80
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")

#For Loop
for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

#while loop
j=1
while j<=5:
    print(j)
    #j=j+1
    j+=1
    if j==2:
        break

#switch statement
day=2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
