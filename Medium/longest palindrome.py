def longestPalindromicSubstring(string):
    currentLongest = [0,1]
    for i in range(1, len(string)):
        odd = helperPalindrome(string, i-1, i+1)
        even = helperPalindrome(string, i, i+1)
        longest = max(odd, even, key= lambda x:x[1] - x[0])
        currentLongest = max(currentLongest, longest, key= lambda x:x[1] - x[0])
    return string[currentLongest[0]: currentLongest[1]]
        
def helperPalindrome(string, leftidx, rightidx):
    while leftidx >= 0 and rightidx <len(string):
        if string[leftidx] != string[rightidx]:
            break
        leftidx -=1
        rightidx +=1
    return [leftidx+1, rightidx]
x = longestPalindromicSubstring('cbbd')
print(x)