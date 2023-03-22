db = {}
def reg(firstname,email,password):
    db["name"] = firstname
    db["email"] = email
    db["password"] = password
    print("Registration Successfully !!")


def login(email,password):
    if email ==db["email"]:
        if password == db["password"]:
            return db["name"]
        else:
            return "Invalid email or password"
        
    else:
        return "Invalid email or password"
    
status = True
while status:
    menu = """
    
        1) press 1 for registration
        2) press 2 for login
        3) press 3 for exit
    """

    print(menu)

    choice = int(input("Enter Your Choice : "))
    if choice ==1:
        name = input("Enter Your Name : ")
        email = input("Enter Email : ")
        password = input("Enter Password : ")
        reg(name,email,password)
        
    elif choice ==2:
        name = input("Enter Your Name : ")
        email = input("Enter Email : ")
        password = input("Enter Password : ")
        print(login(email,password))

    elif choice ==3:
        status = False

