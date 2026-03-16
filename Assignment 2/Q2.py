number = int(input("Enter a positive int : "))
digitSum = 0

while number > 0:
    digitSum += number % 10
    number //= 10

print(digitSum)