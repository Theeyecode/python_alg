from __future__ import annotations


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> None:
        return self.items.pop()

    def is_empty(self) -> None:
        return self.items == []

    def peak(self) -> None:
        return self.items[-1]

    def get_stack(self) -> None:
        return self.items


def reverse_string(stack, input_str) -> None:
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_string = ""
    while not stack.is_empty():
        rev_string += stack.pop()

    return rev_string


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
stack = Stack()
string = 'Hello'

print(reverse_string(stack, string))
