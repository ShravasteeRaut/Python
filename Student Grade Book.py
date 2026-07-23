students = {
    "Shravastee": 95,
    "Kritika": 92,
    "Maira": 85,
    "Tisha": 88,
    "Simran": 78
}            


total = 0
for score in students.values():
    total += score

average = total / len(students)

print("Student Grades:")
for name, score in students.items():
    print(name, ":", score)

print("\nClass Average: ", average)


top_student = max(students, key=students.get)
print("Highest Scorer:", top_student,  students[top_student])


bottom_student = min(students, key=students.get)
print("Lowest Scorer:", bottom_student, students[bottom_student])


search = input("\nEnter student name to search: ")

grade = students.get(search)

if grade is not None:
    print(search,"'s score is", grade)
else:
    print("Student not found.")