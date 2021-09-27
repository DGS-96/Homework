def replace_items(string, *replace_elements, replace_with=""):
    """A function that replaces all characters "(a, ...)" with "b\""""
    
    result = ""
    for index, element in enumerate(string):
        if element in replace_elements:
            result += replace_with
        else:
            result += string[index]
    return result


if __name__ == "__main__":
    text = "\"abc\" - \'cba\'"
    print(replace_items(text))
    print(replace_items(text, "'"))
    print(replace_items(text, "\"", "\'"))
    print(replace_items(text, "\"", replace_with="'"))
    print(replace_items(text, "'", replace_with="\""))
    print(replace_items(text, "\'", "\"", replace_with="/"))

    print()
    help(replace_items)
