fruit_menu = {}

menu = """
1) Manager
2) Customer
"""

status = True
p_status = True

while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("WELCOME TO FRUIT MARKET MANAGER")
        view = """
        1) Add fruit stock
        2) View fruit stock
        3) Update fruit stock
        
        """
        while p_status:
            spec = {}
            print(view)
            choice = int(input("Enter your choice : "))
            
            if choice==1:
                print("ADD FRUIT STOCK")
                name = input("Enter Fruit Name : ")
                qty = int(input("Enter Qty : "))
                price = int(input("Enter Price : "))

                spec['qty'] = qty
                spec['price'] = price

                fruit_menu[name] = spec

            elif choice==2:
                print("VIEW FRUIT STOCK")
                print(fruit_menu)

            elif choice==3:
                print("UPDATE FRUIT STOCK")
                updatename = input("Enter Fruit Name : ")
                updateqty = int(input("Enter Qty : "))
                updateprice = int(input("Enter Price : "))

                oldqty = fruit_menu[updatename]["qty"]
                fruit_menu[updatename]['qty'] = oldqty + updateqty
                fruit_menu[updatename]['price'] = updateprice

            choice = input("DO YOU WANT TO PERFORM MORE OPERATION PRESS Y FOR YES AND N FOR NO : ")
            
            if choice=="n" or  choice == "N":
                p_status = False
            else:
                p_status = True
            
    else:
        while status:
            print("WELCOME TO FRUIT MARKET")
            cname = input("Enter Fruit Name : ")
            cqty = int(input("Enter Qty : "))
            cprice = fruit_menu[cname]['price'] 

            print("Fruit Name : ",cname)
            print("Qty : ",cqty)
            print("Price to Pay",cprice)

            status = False

            print("THANK YOU FOR PURCHASING")
            
        





                



