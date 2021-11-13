vowel = 'aeiou'


def count_consonant_iterative(input_string):

    count = 0
    for i in range(len(input_string)):
        if input_string[i].lower() not in vowel and input_string[i].isalpha():
            count += 1
    return count


def count_consonant_recursion(input_string, idx=0):
    if input_string == '':
        return 0
    elif input_string[0].lower() not in vowel and input_string[0].isalpha():
        return 1 + count_consonant_recursion(input_string[1:])

    else:
        return count_consonant_recursion(input_string[1:])


print(count_consonant_iterative('abc de'))
print(count_consonant_recursion('xxxx  fffa'))
