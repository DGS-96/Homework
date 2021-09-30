def call_once(function_to_decorate):
	"""The call_once decorator, which runs a function or method once and caches the result.
	All sequential calls to this function return the cached result regardless of the arguments
	"""

	flag = False
	first_cach = None

	def wrapper(*args):
		nonlocal flag
		nonlocal first_cach

		if flag == False:
			first_cach = function_to_decorate(*args)
			flag = True

		return first_cach
	return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == "__main__":
	print(sum_of_numbers(13, 42))
	#>>> 55
	print(sum_of_numbers(999, 100))
	#>>> 55
	print(sum_of_numbers(134, 412))
	#>>> 55
	print(sum_of_numbers(856, 232))
	#>>> 55
