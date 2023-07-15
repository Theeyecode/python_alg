random_string = "ghaucjdkb"
res = ""

for char in random_string:
    if char == 'd':
        res = res[1:]  # Remove character at index 0 from res
    elif char in ['a', 'b', 'c']:
        res += char

print(res)