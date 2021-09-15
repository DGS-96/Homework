# Program for calculating the len of a string without using the `len` function.

# input_string = input("Enter the string:\n> ")
input_string = "The quick brown fox jumps over the lazy dog"
print(f"Input string:\n\"{input_string}\"")

string_length = 0
for _ in input_string:
	string_length += 1

print(f"String length = {string_length}")
