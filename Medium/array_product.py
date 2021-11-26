def arrayOfProducts(array):
    # Write your code here.
    output = []
    for i in range(len(array)):
        y = productSums(array, i)
        output.append(y)

    return output


def productSums(array, index):
    i = 0
    productSum = 1
    while i <= len(array) - 1:
        if i == index:
            i += 1
        else:
            productSum = productSum * array[i]
            i += 1
    return productSum


# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array = [5, 1, 4, 2]
# y = productSums(array, 0)
y = arrayOfProducts(array)
print(y)
