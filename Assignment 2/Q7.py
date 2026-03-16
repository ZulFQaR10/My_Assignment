numbers = []
count = int(input("Enter size numbers : "))

for i in range(count):
    value = int(input("Enter int : "))
    numbers.append(value)

prime_numbers = []

for number in numbers:
    if number > 1:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)

prime_tuple = tuple(prime_numbers)

print(prime_tuple)