name = input("Enter Your Name : ")
m = "Male"
f = "Female"
gen = input("Enter Your Gender : ")
age = int(input("Enter Age : "))
pro = input("Enter Product : ")
print("Current gold price(1 gram) : 5752")
gm = int(input("Enter Gram : "))
rate = gm*5752
print("*"*50)
print("Total Gold Rate : ",rate)
print("Making Charges (1 grm) : 845")
charge = gm*845
print("Total Making Charges : ")
print("*"*50)
ta = rate+charge
print("Total Amount : ",ta)
print("Discount : 25%")
dis = rate*25/100
print("Discount-Amount except (making charges : ",dis)
print("*"*50)
pur = rate+charge-dis
print("Total Net Amount : ",pur)


if gen==m and age>65 and pur>21000:
    extra1 = pur*20/100
    amt = pur-extra1
    print("Discount 20% extra =  ",extra1)
    print("Net Payble : ",amt)
elif gen==m and age>65 and pur>31000:
    extra1 = pur*30/100
    print("Discount 30% extra =  ",extra1)
    print("Net Payble : ",amt)
elif gen==m and age>65 and pur>51000:
    extra1 = pur*50/100
    print("Discount 50% extra =  ",extra1)
    print("Net Payble : ",amt)

if gen==f and age>65 and pur>21000:
    extra1 = pur*25/100
    amt = pur-extra1
    print("Discount 25% extra =  ",extra1)
    print("Net Payble : ",amt)

elif gen==f and age>65 and pur>31000:
    extra1 = pur*35/100
    amt = pur-extra1
    print("Discount 35% extra =  ",extra1)
    print("Net Payble : ",amt)

elif gen==f and age>65 and pur>51000:
    extra1 = pur*40/100
    amt = pur-extra1
    print("Discount 40% extra =  ",extra1)
    print("Net Payble : ",amt)

if age<65 and pur>21000:
    extra1 = pur*15/100
    amt = pur-extra1
    print("Discount 15% extra =  ",extra1)
    print("Net Payble : ",amt)

elif age<65 and pur>31000:
    extra1 = pur*25/100
    amt = pur-extra1
    print("Discount 25% extra =  ",extra1)
    print("Net Payble : ",amt)

elif age<65 and pur>51000:
    extra1 = pur*30/100
    amt = pur-extra1
    print("Discount 30% extra =  ",extra1)
    print("Net Payble : ",amt)






