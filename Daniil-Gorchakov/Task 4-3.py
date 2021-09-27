def my_split(string, separators=(" ",), maxsplit=None):
    """A function that works the same as the str.split method
    (without usingstr.split)"""

    result = []
    temp = ""
    split = 0
    for index, item in enumerate(string):
        if item in separators:
            result.append(temp)
            temp = ""
            split += 1
            if split == maxsplit:
                result.append(string[index+1:])
                return result
        else:
            temp += item
    result.append(temp)
    return result


if __name__ == "__main__":
    text1 = "The_quick_brown-fox"
    text2 = "The quick brown fox jumps over the lazy dog"
    print(my_split(text1, "_"))
    print(my_split(text1, ("_", "-")))
    print(my_split(text2))
    print(my_split(text2, maxsplit=1))
    print(my_split(text2, maxsplit=3))
