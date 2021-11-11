from stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    if p1 == "<" and p2 == ">":
        return True
    else:
        return False


def check_parenthesis(balanced_string):
    s = Stack()
    index = 0
    is_balanced = True

    while index < len(balanced_string) and is_balanced:
        peren = balanced_string[index]

        if peren in "([{<":
            s.push(peren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, peren):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(check_parenthesis("{})"))
