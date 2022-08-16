class Solution(object):
    def reverse(self, x):
        s = str(x)
        if s[0] == '-':
            s = s[1:] + '-'
        out = int(s[::-1])
        return 0 if (out > 2**31 - 1) or (out < -2**31) else out
        