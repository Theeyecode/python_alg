def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-2) + getNthFib(n-1)


y = getNthFib(12)
print(y)


# this program gets the nth term of a number in a fib sequence

# 0,1,1,2,3,5,8,13,21,34,55,89
# 1,2,3,4,5,6,7,08,09,10,11,12,13
