class MyContextManager():
	"""Class-based context manager for opening and working
	with file, including handling exceptions"""
	def __init__(self, file_path, mode="r"):
		self.path = file_path
		self.mode = mode

	def __enter__(self):
		self.file = open(self.path, self.mode)
		return self.file

	def __exit__(self, exception_type, exception_value, exception_traceback):
		if exception_type is not None:
			print("Exception:")
			print(f"\tType: {str(exception_type)}")
			print(f"\tValue: {exception_value}")
			print(f"\tTraceback: {exception_traceback}\n")
		self.file.close()
		return True


if __name__ == "__main__":
	with MyContextManager("test_7-1.txt", "w") as file:
		file.write("hello_friend")

	with MyContextManager("test_7-1.txt", "r") as file:
		file.write("hello_friend")
