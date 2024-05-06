anagram = {}
words = ["pear", "amleth", "dormitory", "tinsel", "dirty room", "hamlet", "listen", "silnet"]
for w in words:
    sorted_word = ''.join(sorted(w.replace(" ",'')))
    if sorted_word in anagram:
        anagram[sorted_word].append(w)
    else:
        anagram[sorted_word] = [w]

group_v = []
for group in anagram.values():
    group.sort()
    # group_v.append(group)
    group_v.append(','.join(group))

group_v.sort() 
print(group_v)
