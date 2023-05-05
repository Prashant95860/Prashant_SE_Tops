l = [1,3,5,4,7]
with open('file.txt',"w") as myfile:
    for c in l:
        myfile.write("%s\n"%c)

c = open('file.txt')
print(c.read())