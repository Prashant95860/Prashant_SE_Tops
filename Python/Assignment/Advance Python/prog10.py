f = open('file.txt',"r")
call = f.read()
w = call.split()
print("The number of words in text file : ",len(w))
f.close()