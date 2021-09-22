# A function that splits the string "s" at the indices specified in "indexes"

def split_by_index(s, indexes):
    indexes.sort()
    length_s = len(s)

    temp = []
    for num in indexes:
        if num < length_s:
            temp.append(num)
    indexes = temp

    length = len(indexes) + 1
    indexes.append(length_s)
    indexes.insert(0, 0)
    
    cnt = 0
    index = 0
    output_list = []
    while cnt < length:
        output_list.append(s[indexes[index]:indexes[index+1]])
        index += 1
        cnt += 1
    
    return output_list


if __name__ == "__main__":
    print(split_by_index("pythoniscool,isn'tis?", [6, 8, 12, 13, 18]))
    # ["python", "is", "cool", ",", "isn't", "it?"]
    print(split_by_index("noluck", [42]))
    # ["no luck"]
    print(split_by_index("noluck", [2, 48, 42]))
 