string = input("Enter String : ")
w = input("Enter Word : ")
a = []
count = 0

a = string.split(" ")
for i in range(0,len(a)):
    if (w==a[i]):
        count = count+1
print("Count of Word is : ",count)