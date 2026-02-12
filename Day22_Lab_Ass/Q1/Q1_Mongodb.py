from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]

# Insert new employee
collection.insert_one({
    "name": "Bhagyashree",
    "department": "IT",
    "salary": 55000
})

print("Employee inserted")

#  Find all IT employees
print("\nIT Employees:")
for emp in collection.find({"department": "IT"}):
    print(emp)

#  Update salary of Bhagyashree
collection.update_one(
    {"name": "Bhagyashree"},
    {"$mul": {"salary": 1.10}}
)

print("\nSalary updated by 10%")

client.close()
