from collections import  deque

stack = []
stack.append('A')
stack.append('E')
stack.append('D')
stack.append('C')
print(stack)
stack.pop()
print(stack)


d = deque()
d.append(1)
d.append(5)
d.append(3)
d.append(7)
d.appendleft(6)
print(d)

print(d)