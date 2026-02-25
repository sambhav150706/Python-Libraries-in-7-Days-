import numpy as np

print("===== DAY 03: NUMPY =====")

# 1️⃣ Creating Array
arr = np.array([10, 20, 30, 40])
print("\nArray:", arr)

# 2️⃣ 2D Array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", matrix)

# 3️⃣ Operations
print("\nAdd 5:", arr + 5)
print("Multiply by 2:", arr * 2)

# 4️⃣ Useful Functions
numbers = np.array([5, 10, 15, 20])
print("\nMean:", np.mean(numbers))
print("Sum:", np.sum(numbers))
print("Max:", np.max(numbers))
print("Min:", np.min(numbers))

# 5️⃣ Indexing & Slicing
print("\nFirst Element:", arr[0])
print("Slice 1-3:", arr[1:3])

# 6️⃣ Special Arrays
print("\nZeros:", np.zeros(3))
print("Ones:", np.ones(4))
print("Range:", np.arange(1, 10))

# 7️⃣ Mini Project – Marks Analysis
marks = np.array([78, 85, 90, 66, 88])

print("\n--- Marks Analysis ---")
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Students Scored Above 70:", marks[marks > 70])

print("\nProgram Completed 🚀")