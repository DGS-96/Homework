class Counter():
	"""A counter class that additionally accepts an initial value and a counter stop value.
	The default start is 0.
	If no stop value is specified, the count will continue indefinitely.
	If the counter reaches the stop value, the message "Maximum value reached"."""
	def __init__(self, start=0,  stop=-1):
		self.present_value = start
		self.stop = stop

	def increment(self):
		if self.present_value == self.stop:
			print("Maximal value is reached.")
			raise Exception("Maximal value is reached.")
		else:
			self.present_value += 1

	def get(self):
		#print(f"{self.present_value = }")
		print(self.present_value)

		
if __name__ == "__main__":
	c = Counter(start=42)
	c.increment()
	c.get()
	#>>> 43
	print()

	c = Counter()
	c.increment()
	c.get()
	#>>> 1
	c.increment()
	c.get()
	#>>> 2
	print()

	c = Counter(start=42, stop=43)
	c.increment()
	c.get()
	#>> 43
	c.increment()
	#>>> Maximal value is reached.
	c.get()
	#>>> 43
	print()

	test = Counter()
	for _ in range(10):
		test.increment()
	test.get()
