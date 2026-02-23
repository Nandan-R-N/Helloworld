students = {}

# Add student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    students[roll] = name
    print("Student added successfully!")

# Display students
def display_students():
    print("\nStudent Records:")
    for roll in students:
        print("Roll No:", roll, "Name:", students[roll])

# Main program
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
