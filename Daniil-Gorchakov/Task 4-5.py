def get_digits(num): # -> tuple[int]
	"""A function that returns a tuple of numbers by a given integer"""
	
    return tuple(map(int, (str(num))))


if __name__ == "__main__":
    print(get_digits(87178291199))
	# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
