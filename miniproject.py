# Add student and save to file
def add_student():
    try:
        roll = input("Enter Roll No: ").strip()
        name = input("Enter Name: ").strip()

        if roll == "" or name == "":
            raise ValueError("Roll No and Name cannot be empty.")

        # Check duplicate roll number
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    existing_roll = line.strip().split(",")[0]
                    if roll == existing_roll:
                        print("Roll number already exists!")
                        return
        except FileNotFoundError:
            pass  # File doesn't exist yet

        with open("students.txt", "a") as file:
            file.write(roll + "," + name + "\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)


# Read and display students from file
def display_students():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No records available.")
                return

            print("\nStudent Records:")
            for line in lines:
                parts = line.strip().split(",")

                if len(parts) == 2:   # Prevent crash
                    roll, name = parts
                    print("Roll No:", roll, "Name:", name)
                else:
                    print("Invalid record found in file.")

    except FileNotFoundError:
        print("No records found.")


# Main program
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")