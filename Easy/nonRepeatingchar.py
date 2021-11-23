def firstNonRepeatingCharacter(string):
    # Write your code here.
    characterdictionary = dict()
    for character in string:
        if character not in characterdictionary:
            characterdictionary[character] = 0
        characterdictionary[character] += 1

    for idx in range(len(string)):
        char = string[idx]
        if characterdictionary[char] == 1:
            return idx
    return -1


y = firstNonRepeatingCharacter('abcaa')
print(y)
