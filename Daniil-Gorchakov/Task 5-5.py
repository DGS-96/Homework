def remember_result(function_to_decorate):
	"""A decorator that remembers the last input, decorates the function result
	and prints it out before the next call"""

	last_result = None
	
	def wrapper(*args):
		nonlocal last_result
		print(f'Last result = \'{last_result}\'')
		last_result = function_to_decorate(*args)

	return wrapper		

@remember_result
def sum_list(*args):
	# Validating string and integer input

	if isinstance(args[0], int):
		result = 0
	else:
		result = ""

	for item in args:
		result += item
	print(f"Current result = '{result}'\n")

	return result


if __name__ == "__main__":
	sum_list("a", "b")
	# >>> "Last result = 'None'"
	# >>> "Current result = 'ab'"
	sum_list("abc", "cde")
	# >>> "Last result = 'ab'" 
	# >>> "Current result = 'abccde'"
	sum_list(3, 4, 5)
	# >>> "Last result = 'abccde'" 
	# >>> "Current result = '12'"
