employee_names = []
count = int(input("How many employees : "))

for i in range(count):
    name = input("Enter employee name : ")
    employee_names.append(name)

employee_names.sort()

print(employee_names)