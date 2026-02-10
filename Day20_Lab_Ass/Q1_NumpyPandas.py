import pandas as pd
import numpy as np

students = [
{"name": "Alice", "score": 85},
{"name": "Bob", "score": 92},
{"name": "Charlie", "score": 78},
{"name": "David", "score": 90},
{"name": "Eva", "score": 88}
]

# 1. Convert list of dictionaries to Pandas DataFrame
df = pd.DataFrame(students)
print("Dataframe:",df)

# 2. Calculate mean, median, and standard deviation using NumPy
scores = df["score"].values
print("Mean",np.mean(scores))
print("Median",np.median(scores))
print("Standard Deviation",np.std(scores))


# 3. Add 'above_average' column
df["above_average"] = df["score"] > np.mean(scores)

print(df)
