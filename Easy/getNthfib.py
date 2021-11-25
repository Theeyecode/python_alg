# Using recrusion
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-2) + getNthFib(n-1)

# using iteration
def getNthFib(n):
    fibseq = [0, 1]

    count = 0

    while count <= n-2:  #n-2 since we already have 2 element ...
        # then ignore the first count or use n-3
        if count == 0:
            pass
        else:
            firstelement, secondelement = fibseq[0], fibseq[1]
            nextseq = firstelement + secondelement
            del fibseq[0]
            fibseq.append(nextseq)
            print(count, fibseq[0], fibseq[1])

        count += 1
    return fibseq[1] if n>1 else return fibseq[0]   #catches if n = 0,


y = getNthFib(0)
print(y)


# this program gets the nth term of a number in a fib sequence

# 0,1,1,2,3,5,8,13,21,34,55,89  -> Fibonacci sequence
# 1,2,3,4,5,6,7,08,09,10,11,12
