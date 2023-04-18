s = "w3resource"
d = {}
for letter in s:
    d[letter] = d.get(letter,0) + 1
print(d)


