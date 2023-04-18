d = {1:10,2:20}
d1 = {3:30,4:40}
d2 = {}

for dic in (d,d1) : d2.update(dic)
print(d2)
