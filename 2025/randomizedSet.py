import random


class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.list = []
    def insert(self, val: int) -> bool:
        res = val not in self.hashMap
        if res:
            self.hashMap[val] = len(self.list)
            self.list.append(val)
        return res
    def remove(self, val: int) -> bool:
        res = val in self.hashMap
        if res:
            idx = self.hashMap[val] #get Index of element to remove
            lastVal = self.list[-1]  #get the Last element in the List
            self.list[idx] = lastVal  #update the index of the value to be removed with the last Value
            self.list.pop()    # pop the lastvalue to avoid duplicacy
            self.hashMap[lastVal] = idx   #update the value of the lastVal in the hashMap with its new index in the list
            del self.hashMap[val]   #safely delete the val from hashMap
        return res
    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()