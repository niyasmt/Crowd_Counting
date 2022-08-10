a = [1, 2, 3, 4, 1, 2]

count = 1
s = {}

for i in a:
    if i in s:
        s[i] = s[i] + 1

    else:
        s[i] = count

print(s)