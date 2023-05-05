f = open('file.txt',"r")
call = f.readlines()
print(call[-1])
f.close()