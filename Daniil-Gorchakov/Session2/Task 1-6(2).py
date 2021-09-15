# A program that nicely prints out a part of the multiplication table.

# x_start, x_end = int(input("Enter the start of the first range:\n> ")), int(input("Enter the end of the first range:\n> "))
x_start = 3
x_end = 7

# y_start, y_end = int(input("Enter the start of the second range:\n> ")), int(input("Enter the end of the second range:\n> "))
y_start = 2
y_end = 4

print(f"Table: [{x_start}; {x_end}] * [{y_start}; {y_end}]\n")
len_table = ((x_end - 1) * 4 + x_end - 1)

table = []
temp = [" "]
for x in range(x_start, x_end + 1):
	temp.append(x)
table.append(temp)
temp = []

for y in range(y_start, y_end + 1):
	temp.append(y)
	for x in range(x_start, x_end + 1):
		temp.append(x * y)
	table.append(temp)
	temp = []

# Nice table print
for line in table:
	for num in line:
		print("{: ^4}".format(num), end="|")
	print()
	print("-" * len_table)
