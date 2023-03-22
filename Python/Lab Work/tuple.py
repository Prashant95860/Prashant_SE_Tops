t = (10,20,30)
print(type(t))

t = ("python","java","flutter","java")
print(t)
#for item in t:
    #print(item)
    #print(item,end=",")
    #print(len(t))
#print(t.count("java"))

l1 = list(t)
l1[0] = "React"
t = tuple(l1)
print(t)