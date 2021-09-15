# Displays all divisors of the entered number

# input_number = int(input("Enter an integer:\n> "))
input_number = 60
print(f"Input number = {input_number}")

print(f"Divisors of {input_number}:")
divisors = []
for number in range(1, input_number + 1):
	if input_number % number == 0:		
		divisors.append(number)

print(*divisors)
