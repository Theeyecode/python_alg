def minimumWaitingTime(queries):
    queries.sort()
    waitingTime = 0

    for idx, element in enumerate(queries):
        remainingLen = len(queries) - (idx + 1)
        waitingTime += (element * remainingLen)

    return waitingTime


data = [3, 2, 1, 2, 6]

y = minimumWaitingTime(data)
print(y)
