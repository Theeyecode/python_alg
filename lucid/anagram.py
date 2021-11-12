# 2 ways in checking if there exist an anagram between two strings
# brute approach

# ss1 = 'Fairy tales'
# ss2 = 'rails afety'
ss1 = 'Fairy tales '
ss2 = 'rail safety'
# s1 = s1.replace(" ", "").lower()
# s2 = s2.replace(" ", "").lower()

# print(sorted(s1) == sorted(s2))


def is_anagram(s1, s2):
    hashMemory = dict()

    if len(s1) != len(s2):
        print('len no correlate')
        return False
    for i in s1.lower():
        if i in hashMemory:
            hashMemory[i] += 1
        else:
            hashMemory[i] = 1
    for i in s2.lower():
        if i in hashMemory:
            hashMemory[i] -= 1
        else:
            hashMemory[i] = 1
    for i in hashMemory:
        if hashMemory[i] != 0:
            print(hashMemory[i])

            return False
    print('e reach here')
    return True


print(is_anagram(ss1, ss2))
