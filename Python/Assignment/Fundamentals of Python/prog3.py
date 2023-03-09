nterms=int(input("How many Terms ? : "))
n1,n2 = 0,1
count = 0
if nterms <=0:
    print("Please enter positive value")
elif nterms == 1:
    print("Fibonacci Seires upto : ",a,":")
    print(n1)
else:
    print("Fibonaaci Sequence : ")
while count < nterms:
    print(n1)

    nth = n1+n2
    n1 = n2
    n2 = nth
    count += 1

      

