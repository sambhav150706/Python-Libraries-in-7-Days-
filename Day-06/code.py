import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Sita", "Rahul", "Aman"],
    "Age": [23, np.nan, 25, 23],
    "Salary": [50000, 60000, np.nan, 50000],
    "City": ["Delhi", "Mumbai", "Delhi", "Delhi"]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

# Check missing values
print("\nMissing values:\n")
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nAfter filling missing values:\n")
print(df)

# Remove duplicates
df = df.drop_duplicates()

print("\nAfter removing duplicates:\n")
print(df)

# Rename column
df = df.rename(columns={"Salary": "Income"})

print("\nAfter renaming column:\n")
print(df)

# Convert data type
df["Age"] = df["Age"].astype(int)

print("\nFinal cleaned dataset:\n")
print(df)