# Introduction to recrusion,
#  This code finds the upper-case character in a given input string


input_str1 = 'Pepsicola'
input_str2 = 'pepsiCola'
input_str3 = 'pepsicola'


def find_uppercase_iterative(input_string):
    for i in range(len(input_string)):
        if input_string[i].isupper():
            return input_string[i]

    return 'No uppercase Letter found'


def find_uppercase_recursive(input_string, idx=0):
    if input_string[idx].isupper():
        return input_string[idx]
    if idx == len(input_string) - 1:
        return 'No uppercase Found'
    return find_uppercase_recursive(input_string, idx+1)


print(find_uppercase_iterative(input_str1))
print(find_uppercase_iterative(input_str2))
print(find_uppercase_iterative(input_str3))

print(find_uppercase_iterative(input_str1))
print(find_uppercase_iterative(input_str2))
print(find_uppercase_iterative(input_str3))
