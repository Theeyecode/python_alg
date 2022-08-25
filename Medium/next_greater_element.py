def nextgreaterElement(nums1, nums2):
    # list of items    
    stack = [] # taking empty stack
    dic = {} # taking empty dic
    for num in nums2: # traverse the elements of nums2
        while stack != [] and num > stack[-1]: # checking stack is not empty and num is greater then last element of the stack.
            print(stack.pop())
            dic[stack.pop()] = num # 
            print(num)
        stack.append(num)
        print(stack)
        # In !st traversal, 1 will be added. 
        # In 2nd traversal, 3>1 = 1:3. 
        # In 3rd traversal, 4 is added.
        # In 4th traversal, 2 is not greater then 4(stack-1). So will just add it too in the stack. 
        # At last dic = {1:3}
        # Stack = [4,2] , vertically stack = [2,4]
        
    res = [] # taking empty list
    for num in nums1: # traversing nums1
        if num in dic: # checking if we have num in dic or not
            res.append(dic[num]) # if we have append the value
        else:
            res.append(-1) # else -1
    return res # returning the result

# Will print the index of 'bat' in list2
x = nextgreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
print(x)