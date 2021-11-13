# this python code check the uniquness of an input string
def normalize(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()


def check_uniqness(input_str):
    normalize(input_str)
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True


def check_uniqness_2(input_str):
    return (len(set(input_str)) == len(input_str))


# input_str = normalize('Helo')
# print('This is the new input_string', input_str)
print(check_uniqness("Helo"))
print(check_uniqness_2("Hello"))
