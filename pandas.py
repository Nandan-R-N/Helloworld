import pandas as pd

# Sample student data
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Student Data:")
print(df)

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe())