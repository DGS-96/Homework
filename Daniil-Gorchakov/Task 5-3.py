def CSV_processing(function_to_decorate):
	def wrapper(file_path, number_of_top_students=1):
		raw_data = open(file_path).readlines()

		headline = raw_data[:1][0].replace("\n", "").split()
		
		data = []
		for item in raw_data[1:]:
			temp = item.replace("\n", "").split(",")
			temp[1], temp[2] = int(temp[1]), float(temp[2])
			data.append(temp)

		return function_to_decorate(headline, data, number_of_top_students)
	return wrapper

@CSV_processing
def get_top_performers(headline, data, number_of_top_students):
	"""Returns names of top performer students"""

	sorted_data = sorted(data, key=lambda x: x[2], reverse=True)

	result =[]
	for people in sorted_data[:number_of_top_students]:
		result.append(people[0])

	return result

@CSV_processing
def sort_by_age(headline, data, number_of_top_students):
	"""The function writes the CSV student information to a new file
	in descending order of age"""
	file = open("sorting student information by age.csv", 'w')
	sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

	print(*headline, file=file)
	for item in sorted_data:
		print(",".join((map(str, item))), file=file)

	file.close()
	return None


if __name__ == "__main__":
	print(get_top_performers("../data/students.csv", 5))
	# ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

	sort_by_age("../data/students.csv")
 
