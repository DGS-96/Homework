class HistoryDict(object):
	"""A custom dictionary that will remember the last 10 changed keys.
	Return these keys using the get_history method."""
	def __init__(self, dict):
		self.dict = dict
		self.history = []

	def set_value(self, key, value):
		self.dict[key] = value
		if len(self.history) == 10:
			self.history.pop(0)
			self.history.append(key)
		else:
			self.history.append(key)

	def get_history(self):
		print(self.history)
		

if __name__ == "__main__":
	d = HistoryDict({"foo": 42})
	d.set_value("bar", 43)
	d.get_history()
	#>>> ["bar"]


	for _ in range(9):
		d.set_value("baz", 44)
	d.get_history()

	d.set_value("ten", 10)
	d.get_history()
	d.set_value("eleven", 11)
	d.get_history()
