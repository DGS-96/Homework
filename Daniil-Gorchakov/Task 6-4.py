class Bird():
	"""Bird hierarchy"""
	def __init__(self, name, ration=None):
		self.name = name
		self.ration = ration

	def walk(self):
		print(f"{self.name} bird can walk")

	def eat(self):
		print(f"It eats mostly {self.ration}")

	def fly(self):
		print(f"{self.name} can fly")


class FlyingBird(Bird):
	def __init__(self, name, ration='grains'):
		super().__init__(name, ration)

	def __str__(self):
         return str(f"{self.name} can walk and fly")


class NonFlyingBird(FlyingBird):
	def __init__(self, name, ration='Seed'):
		super().__init__(name, ration)
		
	def swim(self):
		print(f"{self.name} bird can swim")

	def fly(self):
		print(f"AttributeError: '{self.name}' object has no attribute 'fly'")

	def __str__(self):
         return str(f"{self.name} can walk and swim")


class SuperBird(NonFlyingBird):
	def __init__(self, name, ration='fish'):
		super().__init__(name, ration)

	# Redefine the function eat is for another output
	def eat(self):
		print(f"It eats {self.ration}")

	def fly(self):
		super(FlyingBird, self).fly()

	def __str__(self):
         return str(f"{self.name} bird can walk, swim and fly")


if __name__ == "__main__":
	b = Bird("Any")
	b.walk()
	#>>> "Any bird can walk"

	p = NonFlyingBird("Penguin", "fish")
	p.swim()
	#>>> "Penguin bird can swim"
	p.fly()
	#>>> AttributeError: 'Penguin' object has no attribute 'fly'
	p.eat()
	#>>> "It eats mostly fish"
	print(p)
	print()

	c = FlyingBird("Canary")
	print(c) #str(c)
	#>>> "Canary can walk and fly"
	c.eat()
	#>>> "It eats mostly grains"

	s = SuperBird("Gull")
	print(s) #str(s)
	#>>> "Gull bird can walk, swim and fly"
	s.eat()
	#>>> "It eats fish"

	print(SuperBird.__mro__)

	print()
	s.walk()
	s.swim()
	s.fly()