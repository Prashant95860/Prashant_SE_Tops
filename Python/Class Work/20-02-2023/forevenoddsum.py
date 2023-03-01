n = int(input("Enter Number : "))
evensum = 0
oddsum = 0
for i in range (1,n+1):
    if i%2==0:
        print("Even : ",i)
        evensum=evensum+i
    else:
        print("Odd : ",i)
        oddsum=oddsum+i

print("Sum of Even : ",evensum)
print("Sum of Odd : ",oddsum)

    
    #print(i)
