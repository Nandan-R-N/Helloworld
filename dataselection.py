import pandas as pd


data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

# Display full dataset
print("Full Dataset:")
print(df)

# Select specific column
print("\nSelected Column (Name):")
print(df["Name"])

# Select specific rows
print("\nSelected Rows (first two rows):")
print(df.iloc[0:2])

# Select specific rows and columns
print("\nSelected Rows and Columns:")
print(df.loc[0:1, ["Name", "Marks"]])