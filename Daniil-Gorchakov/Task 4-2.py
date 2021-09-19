# A function that checks if a string is palindrome or not.

def palindrome(string):
    string = string.lower()
    string_length = len(string)
    half = int(string_length / 2)

    if string_length % 2 == 0:
        if string[:half] == string[:half-1:-1]:
            return True
        return False
    elif string[:half] == string[:half:-1]:
        return True
    return False

if __name__ == "__main__":
    example = "Madam"
    print(palindrome(example))
    example = "noon"
    print(palindrome(example))
    example = "noons"
    print(palindrome(example))
