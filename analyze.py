import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya"],
    "Marks": [85, 90, 78, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Basic analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# Bar Chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks (Bar Chart)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Line Graph
plt.plot(df["Name"], df["Marks"])
plt.title("Student Marks Trend (Line Graph)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()