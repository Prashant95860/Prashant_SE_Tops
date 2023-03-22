def addition():
    num1 = int(input("Enter Number : "))
    num2 = int(input("Enter Number : "))
    ans = num1 + num2
    print(ans)

def mul():
    num1 = int(input("Enter Number : "))
    num2 = int(input("Enter Number : "))
    ans = num1 * num2
    print(ans)


def menu():
    data = """
    
                Menu

            press 1 for addition
            press 2 for multiplication
    """
    print(data)

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        addition()
    elif choice == 2:
        mul()


menu()