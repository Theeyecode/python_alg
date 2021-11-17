# willnstart sorting
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 33]


def intersection_sorted_list(A, B):
    i = 0
    j = 0
    new_list = []

    while i < len(A) and j < len(B):

        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            if i == 0 or A[i] != A[i-1]:  # OR if not A[i] in new_list
                new_list.append(A[i])
            else:
                pass

            i += 1
            j += 1

    return new_list


print(intersection_sorted_list(A, B))
