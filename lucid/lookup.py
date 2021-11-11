def next_number(s):
    result = []  # a list to store the result
    i = 0  # to got through the index of the string
    while i < len(s):
        count = 1
        # check if we have strings that follow each other eg 11, 22
        while i+1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)


def generate_next_result(s, number_of_times):

    for i in range(number_of_times - 1):
        s = next_number(s)
    return s
