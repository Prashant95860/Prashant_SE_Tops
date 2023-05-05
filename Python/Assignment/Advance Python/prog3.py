f = open('file.txt','a') 
f.write("\nPython is best programming language")
f.close()

f = open('file.txt','r')
c = f.read()
print(c)
f.close()