def palin(str):
    str = input("Enter String : ")
    if (str==str[::-1]):
        print("The string is palindrome")
    else:
        print("The string is not a palindrome")

print(palin(str))
