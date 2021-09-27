def combine_dicts(*dictionaries):
    """A function, that receives dictionaries{letters: numbers}
    (summ identical keys) and merge them into one dictionary"""

    # Convert dictionary to list with tuple [(key, value), ...]
    temp = []
    for dict in dictionaries:
        temp.extend(list(dict.items()))

    result = {key[0]:0 for key in temp}
    for item in temp:
        result[item[0]] += item[1]

    return result

if __name__ == "__main__":
    dict_1 = {"a": 100, "b": 200}
    dict_2 = {"a": 200, "c": 300}
    dict_3 = {"a": 300, "d": 100}
    print(combine_dicts(dict_1, dict_2))
    # {"a": 300, "b": 200, "c": 300}
    print(combine_dicts(dict_1, dict_2, dict_3))
    # {"a": 600, "b": 200, "c": 300, "d": 100}
