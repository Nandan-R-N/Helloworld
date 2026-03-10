import pandas as pd

# Sample student data
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya", "Ravi"],
    "Subject": ["Maths", "Maths", "Science", "Science", "Maths"],
    "Marks": [85, 90, 78, 88, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Group by Subject and calculate average marks
avg_marks = df.groupby("Subject")["Marks"].mean()

print("\nAverage Marks by Subject:")
print(avg_marks)