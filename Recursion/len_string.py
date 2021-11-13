# This code calculates the length of an input string

def length_string_iterative(input_string):
    count = 0
    for i in input_string:
        count += 1
    return count


def length_string_recursive(input_string, idx=0):
    if input_string == '':
        return False
    return 1 + length_string_recursive(input_string[1:])


print(length_string_iterative("abc"))
print(length_string_recursive("abc"))
