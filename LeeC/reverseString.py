def reverses(s):
    if len(s) == 0:
        return s
    else:
        return reverses(s[1:]) + s[0]


x = reverses("Eyecode")
print(x)

inputStr = 'Geeksforgeeks'
print(inputStr[::-1])
