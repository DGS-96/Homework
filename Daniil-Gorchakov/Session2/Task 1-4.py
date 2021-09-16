# A program for sorting a dictionary by key
# The dictionary can contain any valid keys

def append_sorted_items(old_dictionary, new_dictionary, items_list):
	items_list.sort()
	for item in items_list:
		new_dictionary[item] = old_dictionary[item]

def sorting_dictionary_keys(old_dictionary):
	new_dictionary = {}

	lst_num = []
	lst_str = []
	lst_float = []
	lst_tuple = []
	lst_bytes = []
	lst_complex = []
	lst_frozenset = []

	for key in old_dictionary:
		if isinstance(key, int):
			lst_num.append(key)
		elif isinstance(key, float):
			lst_float.append(key)
		elif isinstance(key, str):
			lst_str.append(key)
		elif isinstance(key, tuple): # No check for nested list in tuple
			lst_tuple.append(key)
		elif isinstance(key, complex):
			lst_complex.append(key)
		elif isinstance(key, bytes):
			lst_bytes.append(key)
		elif isinstance(key, frozenset):
			lst_frozenset.append(key)
		else:
			print("Error, data type not specified for element: {key}")
			break

	# Sorting order:
	append_sorted_items(old_dictionary, new_dictionary, lst_num)
	append_sorted_items(old_dictionary, new_dictionary, lst_float)
	append_sorted_items(old_dictionary, new_dictionary, lst_str)
	append_sorted_items(old_dictionary, new_dictionary, lst_bytes)
	append_sorted_items(old_dictionary, new_dictionary, lst_tuple)
	append_sorted_items(old_dictionary, new_dictionary, lst_frozenset)
	append_sorted_items(old_dictionary, new_dictionary, lst_complex)

	return new_dictionary


if __name__ == "__main__":
	example_dictionary = {"2": "0", 1: 0, 3.0: 0.0, frozenset({4, 5}): 0, 2.1: 0, (5, 6): "tuple", "a":"0", 3+6j: "complex", b"bytes": "b0"}

	# If you change or add an element, you need to sort it again, otherwise the dictionary will not be sorted
	sorted_dictionary = sorting_dictionary_keys(example_dictionary)

	print("Example dictionary:")
	print(example_dictionary)
	print("Sorted dictionary:")
	print(sorted_dictionary) 
