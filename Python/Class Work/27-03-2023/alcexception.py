

# 0 division eror
try:


    # accept number from user
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))

    #calculation
    ans = n1/n2

    # display output
    print(ans)

except:
    print("Invalid Input")


#  if value enterd by user is character then it will show (value error)
# for handle it below code run
try:


    # accept number from user
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))

    #calculation
    ans = n1/n2

    # display output
    print(ans)

except:
    print("Invalid Input")


# this code run for details description of error

try:


    # accept number from user
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))

    #calculation
    ans = n1/n2

    # display output
    print(ans)

except ValueError:
    print("Invalid Input - only 0-9 require")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Invalid Input")



