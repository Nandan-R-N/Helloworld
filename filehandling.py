# Writing student details to a text file

# Take input from user
name = input("Enter Student Name: ")
usn = input("Enter USN: ")
course = input("Enter Course: ")
marks = input("Enter Marks: ")

# Open file in write mode
file = open("student.txt", "w")

# Write details to file
file.write("Student Details\n")
file.write("----------------------\n")
file.write("Name: " + name + "\n")
file.write("USN: " + usn + "\n")
file.write("Course: " + course + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("\nStudent details written successfully!\n")

# Reading the content from file
file = open("student.txt", "r")
content = file.read()
file.close()

print("Reading from file:\n")
print(content)
