# This code converts integer to string without using the str() function

# by using the % and //
# 123 %10 gives 3
# 123 // 10 gives 12

def convert_to_string(input_int):
    if input_int < 0:
        input_int *= -1
    output_str = []
    while input_int > 0:
        x = input_int % 10  # get the last number
        result = chr(ord('0') + x)  # convert it to string
        output_str.append(result)
        input_int //= 10
    output_str = output_str[::-1]
    return ''.join(output_str)


print(convert_to_string(-923))
