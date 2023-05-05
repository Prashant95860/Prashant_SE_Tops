f = open('file.txt',"r")
l = f.readlines()
print(l)
l = [x.strip() for x in l]
print(l)
f.close()