import mysql.connector
host = "localhost"
user = "root"
password = "Akash@8201"
database = "feb2026"

conn=mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
print("Connected to the database successfully")
# query="SELECT * FROM feb2026.emp"
# cursor.execute(query)
# result=cursor.fetchall()

# for row in result:
#     print(row)
query="INSERT INTO `feb2026`.`emp` (`Empid`, `Empname`, `Salary`) VALUES ('5', 'Saanu', '65000');"

cursor.execute(query)
conn.commit()
print("Record inserted successfully")




