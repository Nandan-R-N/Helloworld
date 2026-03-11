import pandas as pd

# Sample student data
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Filter students with marks greater than 80
filtered = df[df["Marks"] > 80]

# Sort the filtered data by Marks
sorted_data = filtered.sort_values(by="Marks")

print("\nFiltered and Sorted Dataset:")
print(sorted_data)