product_menu = {}

menu = """

    press 1 for product mnager
    press 2 for customer
    press 3 for exit
    """

status = True
p_status = True

while status:
    print(menu)
    choice = int(input("Enter Your Choice : "))
    if choice ==1:
        while p_status:
            spec = {}
            print("WELCOME TO PRODUCT MANAGER")
            product_name = input("Enter Product Name : ")
            qty = int(input("Enter Qty : "))
            amount = int(input("Enter Amount : "))

            if product_name in product_menu.keys():
                spec['qty'] = product_menu[product_name]['qty'] + qty
                spec["amount"] = amount
            else:
                spec['qty'] = qty
                spec['amount'] = amount

            product_menu[product_name] = spec

            print(product_menu)

            p_choice = input("Do you want to add more product")
            if p_choice =='n':
                p_status = False
    elif choice == 2:
        print("CUSTOMER")
    else:
        print("THANK YOU FOR USING THIS APPLICATION")
    status = False
            