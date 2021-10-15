# Given two non empty array of integers, check if the second array is a subsequence of the first

# def validateSubsequence(array, sequence):
#     seqidx = 0
#     for n in array:
#         if seqidx == len(sequence):
#             break
#         if sequence[seqidx] == n:
#             seqidx += 1

#     return seqidx == len(sequence)

def validateSubsequence(array, sequence):
    arridx = 0
    seqidx = 0

    while arridx < len(array) and seqidx < len(sequence):
        if sequence[seqidx] == array[arridx]:
            seqidx += 1
        arridx += 1

    return seqidx == len(sequence)


x = validateSubsequence([1, 3, 5, 7, 9, 5, 7], [3, 7, 5])

print(x)
