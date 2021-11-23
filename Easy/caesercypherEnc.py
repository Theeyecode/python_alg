def caesarCipherEncryptor(string, key):
    if key == 0:
        return string
    newLetters = []
    newkey = key % 26
    for i in string:
        newLetters.append(helperfunction(i, newkey))
    return "".join(newLetters)


def helperfunction(letter, key):
    newLetter = ord(letter) + key
    return chr(newLetter) if newLetter <= 122 else chr(96 + newLetter % 122)


y = caesarCipherEncryptor("xyz", 54)
print(y)
