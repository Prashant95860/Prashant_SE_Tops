a = ["one","two","three","four"]
max = len (a[0])
t = a[0]

for i in a :
    if (len (i) > max):
        max = len (i)
        t = i
print("The word with longest length is",t,"and length is",max)