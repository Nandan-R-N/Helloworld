students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}

print("Student Names:")
for name in students.keys():
    print(name)

print("\nMarks:")
for marks in students.values():
    print(marks)

print("\nStudent Names and Marks:")
for name, marks in students.items():
    print(name, ":", marks)
