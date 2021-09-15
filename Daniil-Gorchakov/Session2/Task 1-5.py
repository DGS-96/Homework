# Program for printing all unique values of all dictionaries in a list

example = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique_values = set()
for dictionary in example:
	unique_values.add(tuple(dictionary.values())[0])

print(unique_values)
