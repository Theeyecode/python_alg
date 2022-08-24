import math
class Solution(object):
    def calPoints(self, ops):
        new_list = []
        for operation in ops:
            if operation == 'C':
                new_list.remove(new_list[-1])
            elif operation == 'D':
                new_list.append(new_list[-1]*2)
            elif operation == '+':
                new_list.append(new_list[-1] + new_list[-2])
            else:
                new_list.append(int(operation))
        return sum(new_list)

            

            
            
        