n1=int(input("Enter A : "))
n2=int(input("Enter B : "))
n3=int(input("Enter C : "))
print("A = ",n1,"B = ",n2,"C = ",n3)
if n1>n2:
    if n1>n3:
        print("A is Greater")
    else:
        print("C is Greater")
else:
    if n2>n3:
       print("B is Greater")
    else:
        print("C is Greater")
    