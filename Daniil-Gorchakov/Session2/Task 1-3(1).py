# Unique sorted words in the entered word sequence, separated by commas

def unique_string_words(string, split_item=",", replace_items=""):
	print(f"Input text:\n\"{string}\"")

	temp = string.replace(replace_items, "").split(split_item)
	lst = list(set(temp))
	lst.sort()
	
	print("Unique words:")
	print(", ".join(lst))

# Simple input without separating and replacing elements
# unique_string_words(input("Enter a sequence of words separated by commas:\n> "))
unique_string_words("The, quick, brown,  brown, fox,fox,fox", ",", " ")
print()
unique_string_words("The quick brown brown fox fox fox", " ")
