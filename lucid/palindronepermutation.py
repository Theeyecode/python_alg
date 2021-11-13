def isPalindrome_permutation(s):  # doesnt matter in the order,
    hashMemory = dict()
    s = s.replace(" ", '')
    s = s.lower()

    for i in s:
        if i in hashMemory:
            hashMemory[i] += 1
        else:
            hashMemory[i] = 1
    odd_count = 0  # Takes note of the number of odds, you can have 1 letter that doesnt appear twice..i.e the letter in the middle
    for k, v in hashMemory.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1    # first odd...lets check for 2nd
        elif v % 2 != 0 and odd_count != 0:
            print('Its here')
            return False
    return True


x = isPalindrome_permutation("arracec")
print(x)
