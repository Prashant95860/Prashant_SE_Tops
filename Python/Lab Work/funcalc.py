def add():
    n1 = int(input("Enter Number : "))
    n2 = int(input("Enter Number : "))
    ans = n1 + n2
    print(ans)

def mul():
    n1 = int(input("Enter Number : "))
    n2 = int(input("Enter Number : "))
    ans = n1 * n2
    print(ans)

def menu():
    data = """
                 Menu

            press 1 for Addition
            presss 2 for Multiplication

    """
    print(data)
    
    choice = int(input("Enter your choice : "))

    if choice == 1:
        add()
    elif choice == 2:
        mul()

menu()    