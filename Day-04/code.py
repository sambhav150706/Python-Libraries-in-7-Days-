# ================================
# Day-04: Pandas Complete Practice
# ================================

import pandas as pd

print("========== CREATE DATAFRAME ==========\n")

# Creating a DataFrame from dictionary
data = {
    "Name": ["Aman", "Sita", "Rahul", "Neha", "Arjun"],
    "Age": [22, 21, 23, 20, 24],
    "Marks": [85, 90, 78, 88, 76]
}

df = pd.DataFrame(data)

print("Full DataFrame:\n")
print(df)


# =====================================
print("\n========== BASIC INFORMATION ==========\n")

print("First 5 rows:\n")
print(df.head())

print("\nData Information:\n")
print(df.info())

print("\nStatistical Summary:\n")
print(df.describe())


# =====================================
print("\n========== SELECTING COLUMNS ==========\n")

print("Select Name column:\n")
print(df["Name"])

print("\nSelect Name and Marks columns:\n")
print(df[["Name", "Marks"]])


# =====================================
print("\n========== FILTERING DATA ==========\n")

high_marks = df[df["Marks"] > 80]

print("Students with Marks > 80:\n")
print(high_marks)


# =====================================
print("\n========== ADDING NEW COLUMN ==========\n")

df["Grade"] = ["B", "A", "C", "B", "C"]

print(df)


# =====================================
print("\n========== MISSING VALUES EXAMPLE ==========\n")

# Create DataFrame with missing values
data_with_missing = {
    "Name": ["Ravi", "Priya", "Karan", "Anita"],
    "Salary": [50000, None, 45000, None]
}

df2 = pd.DataFrame(data_with_missing)

print("Data with Missing Values:\n")
print(df2)

print("\nCheck Missing Values:\n")
print(df2.isnull())

print("\nCount Missing Values:\n")
print(df2.isnull().sum())


# Fill missing values with mean
df2["Salary"].fillna(df2["Salary"].mean(), inplace=True)

print("\nAfter Filling Missing Values:\n")
print(df2)


# =====================================
print("\n========== SAVING TO CSV ==========\n")

df.to_csv("students.csv", index=False)
print("students.csv file created successfully!")


# =====================================
print("\n========== READING CSV FILE ==========\n")

df_csv = pd.read_csv("students.csv")
print(df_csv.head())


# =====================================
print("\n========== MINI TASK OUTPUT ==========\n")

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())


print("\n========== END OF DAY-04 ==========")