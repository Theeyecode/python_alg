# This code converts integer to string without using the str() function

# by using the % and //
# 123 %10 gives 3
# 123 // 10 gives 12

def convert_to_string(input_int):
    if input_int.isalpha():
        return 'requires an integer value'
    if input_int < 0:
        isNegative = True  # to catch the neegative number
        input_int *= -1
    else:
        isNegative = False
    output_str = []
    while input_int > 0:
        x = input_int % 10  # get the last number
        result = chr(ord('0') + x)  # convert it to string
        output_str.append(result)
        input_int //= 10  # this divides by 10 and remove the remaineder i.e automatically removes the last element because its in base 10
    output_str = output_str[::-1]  # reverse the list
    if isNegative:
        return '-' + ''.join(output_str)
    else:
        return ''.join(output_str)


print(convert_to_string('123'))
