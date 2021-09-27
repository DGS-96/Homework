# Import my_split() from Task 4-3
my_func = __import__("Task 4-3")

def get_shortest_word(s, separators=(" ",)):
    """A function that returns the longest word in the given line"""

    # My custom split from "Task 4-3"
    words = my_func.my_split(s, separators)

    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            result = word
    return result


if __name__ == "__main__":
    print(get_shortest_word("Python is simple and effective!"))
    # 'effective!'
    print(get_shortest_word('Any pythonista like namespaces a lot.'))
    # 'pythonista'    
    print(get_shortest_word("Python-is-simple_and effective!", (" ", "-", "_")))
