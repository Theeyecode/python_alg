def generateDocument(characters, document):
    if len(characters) != len(document):
        return False
    d = dict()

    for char in characters:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for doc in document:
        if doc in d:
            d[doc] -= 1
        else:
            d[doc] = 1

    return all(value == 0 for value in d.values())


y = generateDocument("Bst AEterpx sihet elog!", "AlgoExpert is the Best!")
print(y)
