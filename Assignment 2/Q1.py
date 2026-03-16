Students = [
    ["Ali", 70],
    ["Hassan", 45],
    ["Hussin", 80]
]

Students.insert(2, ["Ahmed", 90])
Students[2] = ["Zain", 95]

passStudents = []

for student in Students:
    name = student[0]
    mark = student[1]
    if mark >= 50:
        passStudents.append([name, mark])

print("Passe Students:")
for student in passStudents:
    print(f"Name : {student[0]}, Mark : {student[1]}")