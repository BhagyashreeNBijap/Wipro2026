import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akash@8201",
    database="company_db"
)
cursor = conn.cursor()

# 1️ Fetch salary > 50000
print("Employees with salary > 50000:\n")

cursor.execute("SELECT * FROM employees WHERE salary > 50000")

for row in cursor.fetchall():
    print(row)

# 2️ Insert new employee
cursor.execute(
    "INSERT INTO employees VALUES (%s, %s, %s, %s)",
    (4, "Bhagyashree", "IT", 55000)
)
conn.commit()
print("\nNew employee inserted")

# 3️ Update salary by 10% for id = 4
cursor.execute(
    "UPDATE employees SET salary = salary * 1.10 WHERE id = 4",

)
conn.commit()
print("Salary updated by 10%")

cursor.close()
conn.close()
