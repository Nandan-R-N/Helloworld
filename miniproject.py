# Add student and save to file
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")

    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "\n")

    print("Student added successfully!")

# Read and display students from file
def display_students():
    try:
        with open("students.txt", "r") as file:
            print("\nStudent Records:")
            for line in file:
                roll, name = line.strip().split(",")
                print("Roll No:", roll, "Name:", name)
    except FileNotFoundError:
        print("No records found.")

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