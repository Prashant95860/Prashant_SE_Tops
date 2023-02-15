roll=int(input("Enter Roll No: "))
name=input("Enter Name: ")
py=int(input("Enter Physics Marks : "))
ma=int(input("Enter Maths Marks : "))
by=int(input("Enter Biology Marks : "))
tot=(py+ma+by)
pr=(tot/3)

print("*"*80)
print()
print("Roll No : ",roll)
print("Name : ",name)
print("Physics Marks : ",py)
print("Maths Marks : ",ma)
print("Biology Marks : ",by)
print("Tota : ",tot)
print("Percentage : ",pr)

if pr>=75:
    print("Distinction.")
elif pr>=60:
    print("First Class.")
elif pr>=50:
    print("Second Class.")
elif pr>=40:
    print("Pass.")
else:
    print("Fail")

