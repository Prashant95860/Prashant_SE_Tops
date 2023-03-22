jay_bhavani = {
    "vadapav" : 30,
    "bhel" : 40,
    "dabeli" : 20
    }

print("*"*10,"Menu","*"*10)

for k,v in jay_bhavani.items():
    print(f"{k} = {v}")

print("*"*20)

cart = {}

status = True

while status:
    product_name = input("Enter Product Name : ").lower()
    qty = int(input("Enter Qty : "))
    
    price = qty*jay_bhavani[product_name]
    print("Price of Your Order : ",price)
    
    cart[product_name] = price
    
    choice = input("Do you want to purchase more product : press Y for Yes and N for No")
    if choice =="n" or choice=="N":
        status = False
        print(cart)
