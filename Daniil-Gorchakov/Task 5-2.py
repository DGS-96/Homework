import string

def most_common_words(filepath, number_of_words=3):
	"""Search function for the most common words in a file"""

	global chars_list
	file = open(filepath).read().lower()

	# List of characters without space
	all_chars_in_file = set(file)
	file_symbols = all_chars_in_file - chars_list
	file_symbols.discard(" ")

	# Clear and create a list
	for symbol in file_symbols:
		file = file.replace(symbol, "")
	file = file.split()

	# Count the number of repetitions
	words = {}
	for word in file:
		if word not in words:
			words[word] = 1
		else:
			words[word] += 1

	sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)

	result = []
	for word in sorted_words[:number_of_words]:
		result.append(word[0])

	return result


chars_list = set(string.ascii_lowercase)

if __name__ == "__main__":
	print(most_common_words('../data/lorem_ipsum.txt'))
	# >>> ['donec', 'etiam', 'aliquam']
