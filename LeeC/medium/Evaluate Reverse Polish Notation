class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operators = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t in valid_operators: 
                first = stack.pop()
                second = stack.pop()
                arithmetic = self.performOperator(first, second, t)
                stack.append(arithmetic)
            else:
                stack.append(int(t))
        return stack[-1]
    
    def performOperator(self,a,b, operator):
        if operator == '+':
            return a + b
        if operator == '-':
            return b - a
        if operator == '*':
            return a * b
        if operator == '/':
            return int(b/a)














