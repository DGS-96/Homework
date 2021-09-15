# Program to convert a given tuple of positive integers to an integer

# input_tuple = tuple(input("Enter a tuple:\n> "))
input_tuple = (3, 2, 1, 6)
print(f"Input tuple = {input_tuple}")

number = int("".join(map(str, input_tuple)))

print(f"Output number = {number}")
