jay_bhavani = {

    "vadapav" : 30,
    "dabeli" : 20,
    "bhel" : 70,
    }

print("Menu")
for k,v in jay_bhavani.items():
    print(f"{k} Rs. {v}")


cart = {}

status = True

while status:
    product_name = input("Enter Product Name : ").lower()
    qty = int(input("Enter qty : "))

    price = qty*jay_bhavani[product_name]
    print("Price of your order : ",price)

    cart[product_name] = price

    choice = input("Do you want to purchase more product : press Y for Yes and N for No")
    if choice =="n" or choice=="N":
        status = False
        print(cart)
