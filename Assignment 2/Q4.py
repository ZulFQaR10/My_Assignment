n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

maxNum = n1

if n2 > maxNum:
    maxNum = n2

if n3 > maxNum:
    maxNum = n3

print(maxNum)