from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["Company_DB"]
collection = db["employee"]

# 🔹 Insert new document
employee = {
    "emp_id": 2,
    "name": "Bhagya",
    "salary": 65000,
    "department": "IT",
}

collection.insert_one(employee)

print("New document inserted successfully\n")


for emp in collection.find():
    print(emp)

# Close connection
# client.close()    
