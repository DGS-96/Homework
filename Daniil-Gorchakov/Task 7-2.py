from contextlib import contextmanager

@contextmanager
def open_file(path, mode="r"):
	try:
		file = open(path, mode)
		yield file
	except:
		print("Some mistakes")
	finally:
		file.close()


if __name__ == "__main__":
	with open_file("test_7-2.txt", 'w') as file:
		file.write("hello")

	with open_file("test_7-2.txt", 'r') as file:
		file.write("world")
