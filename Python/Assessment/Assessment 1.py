fruit_menu = {}
update_menu = {}



menu = """

     1)Manager
     2)Customer 
     
    """

status = True
p_status = True
r_status = True

while status:
    print(menu)
    choice = int(input("Enter Your Choice : "))
    if choice ==1:
            print("WELCOME TO FRUIT MARKET MANAGER")
            view = """
                1) Add Fruit Stock
                2) View Fruit Stock
                3) Update Fruit Stock
            
            """
            while p_status:
                  
                print(view)
                choice = int(input("Enter Your Choice : "))

                if choice==1:
                    print("ADD FRUIT STOCK")
                    name = input("Enter Fruit Name : ")
                    qty = int(input("Enter Qty : "))
                    price = input("Enter Price : ")

                    choice = input("DO YOU WANT TO PERFORM MORE OPERATION : PRESS Y FOR YES AND N FOR NO : ")
                    if choice=="N" or "n":
                         status = False
                        
                elif choice==2:
                    print("VIEW FRUIT STOCK")
                    fruit_menu["name"] = name 
                    fruit_menu["qty"] = qty
                    fruit_menu["price"] = price
                    
                    print(fruit_menu)
                    print(update_menu)
                
                elif choice==3:
                     print("UPDATE FRUIT STOCK")
                     updateqty = int(input("Enter Qty : "))
                     updateprice = input("Enter Price : ") 
                     update_menu["Qty"]=updateqty
                     update_menu["Price"]=updateprice


    else:
         print("WELCOME TO FRUIT MARKET")
         cname = input("Enter Fruit Name : ")
         cqty = int(input("Enter Qty : "))
         print(cname)
         print(cqty)

         status = False

         print("THANK YOU FOR PURCHASING")
        
         
                

                     






            
                  
                  
                  








            