# this code convert a numeric string "123" to an integer 123 without using the "int" function

def str_to_int(input_str):
    output_int = 0
    if input_str[0] == '-':
        start_index = 1
        is_Negative = True
    else:
        start_index = 0
        is_Negative = False
    x = len(input_str)

    for i in range(start_index, x):
        output = 10**(x - (i+1))
        output_int += output * (ord(input_str[i]) - ord('0'))

    if is_Negative:
        return -1 * output_int
    else:
        return output_int


x = (str_to_int('-1123'))
print(x)
