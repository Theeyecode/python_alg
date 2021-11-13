s = "Chinedu should 1fuck off"
s = ''.join([i for i in s if i.isalpha()]).replace(" ", "").lower()
print(s)

print(s == s[::-1])


# def isPalindrome(s):
#     i = 0
#     j = len(s) - 1

#     while i < j:
#         while not s[i].isalnum() and i < j:
#             i += 1
#         while not s[j].isalnum() and i < j:
#             j -= 1
#         if s[i].lower() != s[j].lower():
#             return False

#         i += 1
#         j -= 1
#     return True


# print(isPalindrome("Hx1eexh"))
