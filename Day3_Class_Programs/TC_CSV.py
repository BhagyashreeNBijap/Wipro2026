import csv
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Bhagya",1,20])
    writer.writerow(["Abhi", 2, 21])
    writer.writerow(["Akash", 3, 22])
