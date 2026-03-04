import pandas as pd


data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya"],
    "Age": [20, None, 19, 22],
    "Marks": [85, 90, None, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 🔹 Handle missing values
# Fill missing Age with average Age
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Marks with 0
df["Marks"].fillna(0, inplace=True)

# 🔹 Update dataset (Add Grade column)
df["Grade"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\nUpdated Data:")
print(df)