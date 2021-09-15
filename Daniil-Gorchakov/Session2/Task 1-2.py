# Program for counting frequency of characters in a string (case-insensitive)

def frequency_of_characters(text):
	print(f"Input string:\n\"{text}\"")
	text = text.lower()
	characters = dict((char, 0) for char in text)
	for char in text:
		characters[char] += 1

	sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)

	print("Char - count")
	for char in sorted_characters:
		print(f" \"{char[0]}\" - {char[1]}")


# frequency_of_characters(input("Enter the string:\n> "))
frequency_of_characters("The quick brown fox jumps over the lazy dog")
