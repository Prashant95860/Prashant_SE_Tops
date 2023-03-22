a = input("Enter A : ")
b = input("Enter B : ")
c = a[0:2]
a = a.replace(a[0:2],b[0:2])
b = b.replace(b[0:2],c)
print(a,b)