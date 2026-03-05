import matplotlib.pyplot as plt

# Sample data
subjects = ["Maths", "Science", "English", "Computer"]
marks = [85, 90, 78, 88]

# Bar Chart
plt.bar(subjects, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Line Graph
plt.plot(subjects, marks)
plt.title("Student Marks - Line Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()