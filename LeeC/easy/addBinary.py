class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = (ord(a[i]) - ord('0')) if i < len(a) else 0
            digitB = (ord(b[i]) - ord('0')) if i < len(b) else 0
            total = digitA + digitB + carry
            char = total%2
            carry = total//2
            output = str(char) + output

        if carry:
            output = "1" + output

        return output
