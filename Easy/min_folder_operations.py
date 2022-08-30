def minOperations(log):
    operation = 0;
    for element in log:
        if element != '../' and element!='./':
            operation+=1
            print(element, operation)
        elif element == '../' and operation >0:
            operation-=1
    return operation
    
    
    
    
x = minOperations(["d1/","d2/","../","d21/","./"])
print(x)