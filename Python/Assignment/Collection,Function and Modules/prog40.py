d1 = {"a" : 100,"b" : 200, "c" : 300}
d2 = {"a" : 300,"b" : 200, "d" : 400}

new = d2

for i,j in d1.items():
    if i in d2:
        new[i] = j+d2[i]

    else:
        new[i] = [j]

print(new)
