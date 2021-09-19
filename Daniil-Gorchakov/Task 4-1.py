# A function that replaces all characters "(a, ...)" with "b"

def replace_item(string, *replace_elements, replace_with=""):
    result = ""
    for index, element in enumerate(string):
        if element in replace_elements:
            result += replace_with
        else:
            result += string[index]
    return result

if __name__ == "__main__":
    text = "\"abc\" - \'cba\'"
    print(replace_item(text))
    print(replace_item(text, "'"))
    print(replace_item(text, "\"", "\'"))
    print(replace_item(text, "\"", replace_with="'"))
    print(replace_item(text, "'", replace_with="\""))
    print(replace_item(text, "\'", "\"", replace_with="/"))
