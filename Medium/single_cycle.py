def hasSingleCycle(array):
    # Write your code here.
    n = len(array)
    no_of_element_visited = 0
    currentidx = 0
    if n ==1:
        return True
    while no_of_element_visited < n:
        if no_of_element_visited > 0 and currentidx == 0:
            return False
        no_of_element_visited +=1
        currentidx = helperjump(array, currentidx, n)
    return currentidx == 0
        
        
def helperjump(array, idx, n):
    x = array[idx]
    nextidx = (idx + x) % n
    return nextidx 
        
        
x = hasSingleCycle([2,3,1,-4,-4,2])
print(x)

















