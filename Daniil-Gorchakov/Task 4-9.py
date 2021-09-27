import string

def test_1_1(*strings):
    """Functions that receive a variable number of rows and return the
    characters that appear in all strings"""

    result = set(strings[0])
    for item in strings[1:]:
        result &= set(item)

    return result

def test_1_2(*strings):
    """Functions that receive a variable number of rows and return the
    characters that appear in at least one string"""

    result = set()
    for string in strings:
        result |= set(string)
    return result

def test_1_3(*strings):
    """Functions that receive a variable number of rows and return the
    characters that appear at least in two strings"""

    temp = set(strings[0])
    result = temp.copy()
    for string in strings[1:]:
        temp -= set(string)
    result -= temp
    return result

def test_1_4(*strings):
    """Functions that receive a variable number of rows and return the
    characters of alphabet, that were not used in any string"""

    global chars_list
    used_chars = set()
    for string in strings:
        used_chars = used_chars | set(string)
    return chars_list - used_chars

chars_list = set(string.ascii_lowercase)


if __name__ == "__main__":
    strings = ["hello", "world", "python"]
    print(test_1_1(*strings))
    # {'o'}
    print(test_1_2(*strings))
    # {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
    print(test_1_3(*strings))
    # {'h', 'l', 'o'}
    print(test_1_4(*strings))
    # {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
