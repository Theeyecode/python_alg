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


def secondfunction(string):

    for idx in range(len(string)):
        foundDuplicate = False
        for idx2 in range(idx, len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True

        if foundDuplicate:
            return idx
    return -1


y = secondfunction('akbcaka')
print(y)
