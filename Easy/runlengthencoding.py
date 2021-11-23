def runLengthEncoding(string):
    encodedString = []
    currentLength = 1
    for i in range(1, len(string)):
        currentChar = string[i]
        previousChar = string[i-1]
        if currentChar != previousChar or currentLength == 9:
            encodedString.append(str(currentLength))
            encodedString.append(previousChar)
            currentLength = 0
        currentLength += 1
    encodedString.append(str(currentLength))
    encodedString.append(string[len(string)-1])

    return "".join(encodedString)


y = runLengthEncoding('AAAAAAAAAAAbbbbbc')
print(y)
