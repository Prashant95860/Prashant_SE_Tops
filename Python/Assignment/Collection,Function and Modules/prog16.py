l = [5,6,8,4,2]
sublist = [8,2,7]
c= 0

res = "True"
for i in sublist:
    if i in l:
        c+=1
if (c==len(sublist)):
    res

print("Is sublist present in list : ",res)

