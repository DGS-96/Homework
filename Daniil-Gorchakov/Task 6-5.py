class Sun():
	"""Singleton class that allows only one instance of itself to be created and
	provides access	to this instantiated instance."""
	def inst(self):
		if not hasattr(self, 'inst'):
			self.inst = super().inst(self)
		return self.inst


if __name__ == "__main__":
	p = Sun.inst
	f = Sun.inst
	print(p is f)
	#>>> True

	print()
	print(p)
	print(f)
