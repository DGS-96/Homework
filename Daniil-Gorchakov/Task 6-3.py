class Cipher():
	"""docstring for Cipher"""
	def __init__(self, encode_key):
		self.encode_key = encode_key.lower()
		Cipher.generate_encode_list(self)

	def generate_encode_list(self):
		self.chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		chars = self.chars.copy()
		chars_len = 26 #len(chars)
		self.encode_list = list(self.encode_key)

		for char in self.encode_list:
			chars.remove(char)

		self.encode_list.extend(chars)

	def encode(self, encode_string):
		encode_result = ""
		for char in encode_string:
			if char.lower() not in self.chars:
				encode_result += " "
			else:
				index = self.chars.index(char.lower())
				if char.isupper():
					encode_result += self.encode_list[index].upper()
				else:
					encode_result += self.encode_list[index]
		print(encode_result)

	def decode(self, decode_string):
		decode_result = ""
		for item in decode_string:
			if item.lower() not in self.encode_list:
				decode_result += " "
			else:
				index = self.encode_list.index(item.lower())
				if item.isupper():
					decode_result += self.chars[index].upper()
				else:
					decode_result += self.chars[index]
		print(decode_result)


if __name__ == "__main__":
	cipher = Cipher("crypto")
	cipher.encode("Hello world")
	#>>> "Btggj vjmgp"
	cipher.decode("Fjedhc dn atidsn")
	#>>> "Kojima is genius"

