import numpy as np
import pandas as pd

arr=np.array([10,20,5,6,200])

print("array",arr)
print("sum",np.sum(arr))
print("mean",np.mean(arr))
print("multiply by 2:",arr*2)

data={
    "Name":["Bhagya","Akash","Abhi"],
    "Age":[23,25,27],
    "City":["Bangalore","Hyderabad","Mumbai"]
}

df=pd.DataFrame(data)
print(df)

print(type(df))
print(df["Name"])
print(df["Age"])
print(df["City"])
print(df[df["Age"]>25])

df["Salary"]=[50000,60000,80000]
print(df)
