class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashMap = {}

        for i in s:
            hashMap[i] = hashMap.get(i, 0) +1
        for i in t:
            if i not in hashMap or hashMap[i] == 0:
                return i
            hashMap[i] -=1
        return ''
      # You can also use a Counter:
        counter_s = Counter(s)
        for i in t:
            if not in counter_s or counter_s[i] == 0:
                return i
            else:
                counter_s[i] -=1
        
              
        
