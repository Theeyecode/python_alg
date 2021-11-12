# this code check if a particular string is a permutation of another string   eg..dog and god
def check_permutaion(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    d = dict()

    for i in str_1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1

    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    return all(value == 0 for value in d.values())


def check_permutation_2(str1, str2):
    if (len(str1) != len(str2)):
        return False
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    n = len(str1)

    for i in range(n):
        if str1[i] != str2[i]:
            return False
    return True


print(check_permutaion('hi', 'ih'))
print(check_permutation_2('hi', 'ih'))
