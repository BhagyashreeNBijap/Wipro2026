import pandas as pd

# Create the DataFrame
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)
print("Original dataFrame:")
print(df)

# 1. Filter employees from IT department
it_employees = df[df["Department"] == "IT"]
print("\nEmployees from IT department:")
print(it_employees)

# 2. Find average salary per department
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage salary per department:")
print(avg_salary)

# 3. Add Salary_Adjusted column (10% increase)
df["Salary_Adjusted"] = df["Salary"] * 1.10
print("\n",df)
