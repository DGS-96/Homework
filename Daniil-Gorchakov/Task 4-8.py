# A function that returns a list sets containing pairs of elements

def get_pairs(lst): # list[] -> list[tuple()]
    length = len(lst)
    if length == 1:
        return None
    
    result = []
    for index in range(length - 1):
        result.append((lst[index], lst[index+1]))
    return result

if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8 ,9]))
    # [(1, 2), (2, 3), (3, 8), (8, 9)]
    print(get_pairs(['need', 'to', 'sleep', 'more']))
	# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
    print(get_pairs([1]))
    # None
