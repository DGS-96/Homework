class Sun():
	"""Singleton class that allows only one instance of itself to be created and
	provides access	to this instantiated instance."""
	def inst(self):
		if not hasattr(self, 'inst'):
			self.inst = super().__new__(self)
		return self.inst

class Sun2():
	"""Singleton class that allows only one instance of itself to be created and
	provides access	to this instantiated instance."""
	def __new__(self):
		if not hasattr(self, 'inst'):
			self.inst = super().__new__(self)
		return self.inst


if __name__ == "__main__":
	p = Sun.inst
	f = Sun.inst
	print(p is f)
	#>>> True

	print(p)
	print(f)

	print()
	s1 = Sun2()
	s2 = Sun2()
	print(s1)
	print(s2)
	print(s1 is s2)