def product_twoNum(num1=int, num2=int):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 > num2:
        print('Did this')
        return num1 + product_twoNum(num1, num2-1)
    else:
        print('Did this instead')
        return num2 + product_twoNum(num1-1, num2)


print(product_twoNum(500, 2000))
