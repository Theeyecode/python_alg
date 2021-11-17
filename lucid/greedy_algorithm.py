# Optimal task assignment problem


def greedy(data):
    x = []
    data = sorted(data)
    for i in range(len(data)//2):
        if data[~i] == None:
            x.append([data[i], 0])

        x.append([data[i], data[~i]])

    return x


A = [6, 3, 2, 7, 5, 5, 10, 4]
y = greedy(A)
print(y)
