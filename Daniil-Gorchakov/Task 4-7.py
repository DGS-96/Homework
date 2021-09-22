# A function which is from the list integers, returns a new list,
# each of which is an element with index "i" of the new list is the product of
# all numbers in the original array, except for the number in "i"

from math import prod as multiply_list

def foo(lst):
    copy_lst = lst[:]
    length = len(lst)
    result = []
    for index in range(length):
        copy_lst.pop(index)
        result.append(multiply_list(copy_lst))
        copy_lst = lst[:]

    return result

if __name__ == "__main__":
    print(foo([1, 2, 3, 4, 5]))
    # [120, 60, 40, 30, 24]
    print(foo([3, 2, 1]))
    # [2, 3, 6]
