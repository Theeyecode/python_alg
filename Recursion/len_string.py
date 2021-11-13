# This code calculates the length of an input string

def length_string_recursive(input_string):
    count = 0
    for i in input_string:
        count += 1
    return count


print(length_string_recursive("abc"))
