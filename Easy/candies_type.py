
# Online Python - IDE, Editor, Compiler, Interpreter

def candies(candies):
    candies.sort()
    n = len(candies)
    x = n/2
    count = 1
    for i in range(1,n):
        if candies[i] != candies[i-1]:
            count +=1
    min(x, count)
    



x = candies([6,6,6,6])
print(x)
    
    
