# Sorted names from "data/unsorted_names.txt" in the data folder

names = open("../data/unsorted_names.txt").readlines()
names.sort()

sorted_names = open("sorted_names.txt", "w")

for name in names:
	sorted_names.write(name)

sorted_names.close()
