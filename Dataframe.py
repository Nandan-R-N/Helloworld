import pandas as pd

data = {
    "Name": ["Nandan", "Rahul", "Sneha", "Anjali"],
    "Age": [21, 22, 20, 21],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)


print("Student Data:\n")
print(df)


print("\nSummary of Data:\n")
print(df.describe())
