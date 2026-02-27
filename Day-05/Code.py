# ==========================================
# Day-05: Seaborn Complete Visualization
# ==========================================

# Importing required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

print("========== LOADING DATASET ==========\n")

# Load built-in dataset
df = sns.load_dataset("tips")

print(df.head())

# ==========================================
print("\n========== BASIC INFO ==========\n")

print(df.info())

print("\nStatistical Summary:\n")
print(df.describe())

# ==========================================
print("\n========== SCATTER PLOT ==========\n")

sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total Bill vs Tip")
plt.show()

# ==========================================
print("\n========== HISTOGRAM ==========\n")

sns.histplot(df["total_bill"], bins=20)
plt.title("Distribution of Total Bill")
plt.show()

# ==========================================
print("\n========== BOX PLOT ==========\n")

sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Total Bill by Day")
plt.show()

# ==========================================
print("\n========== BAR PLOT ==========\n")

sns.barplot(x="day", y="total_bill", data=df)
plt.title("Average Total Bill per Day")
plt.show()

# ==========================================
print("\n========== HEATMAP ==========\n")

# Correlation matrix (only numeric columns)
correlation = df.corr(numeric_only=True)

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ==========================================
print("\n========== END OF DAY-05 ==========")
