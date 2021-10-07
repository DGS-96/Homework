def endless_generator():
	"""A generator that will generate odd numbers infinitely"""
    number = 1
    while True:
        yield number
        number += 2


gen = endless_generator()
while True:
    print(next(gen))

#for _ in range(10):
#	print(next(gen))
