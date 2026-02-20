import matplotlib.pyplot as plt


subjects = ["Maths", "Science", "English", "Computer"]
marks = [85, 90, 78, 88]


plt.figure()
plt.bar(subjects, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()


plt.figure()
plt.plot(subjects, marks)
plt.title("Student Marks - Line Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
