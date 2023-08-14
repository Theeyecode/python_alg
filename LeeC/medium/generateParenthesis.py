class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def recursive(openN, closeN):
            if (openN == closeN == n):
                res.append("".join(stack))
                return
            if (openN < n):
                stack.append('(')
                recursive(openN+1, closeN)
                stack.pop()
            if (closeN < openN):
                stack.append(')')
                recursive(openN, closeN+1)
                stack.pop()
        recursive(0,0)
        return res
