l = [10,20,10,20,30,40]
l1 = []
for x in l:
    if x not in l1:
        l1.append(x)

print(l)
print("Unique Numbers :",l1)