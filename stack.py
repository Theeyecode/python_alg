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

# python code to reverse a string using stack.


def reverse_string(stack, input_str) -> None:
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_string = ""
    while not stack.is_empty():
        rev_string += stack.pop()

    return rev_string


# python code to convert binary numbers to integer

def convert_decimal(dec_num=int) -> None:
    new_stack = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        new_stack.push(remainder)
        dec_num = dec_num // 2
    bin_num = ""
    while not new_stack.is_empty():
        bin_num += str(new_stack.pop())
    return bin_num


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(convert_decimal(242))
