print("*"*20,"Welcome to IPL","*"*20)
l = "CSK"
print("Your Name : ",l)
import random

l1 = ["KXIP","KKR","RCB","RR"]
print("Your Opponent : ",random.choices(l1))

print("*"*20,"Toss Time","*"*20)
h = "Head"
toss = input("Press H For Heads and T for Tails : ")

import random
random.choices(toss)
if toss==h:
    print("YOU  WON")
    b = input("Press B for Batting f for Fuilding : ")
else:
    print("Sorry You Loose")
    b = "Batting"
    f = "Bowl"
    print("Opponent Won The toss and selected",b)

print("*"*20,"Ready for Match","*"*20)
if toss==h:
    print("You selected Batting",b)
l2 = [1,2,3,4,6,"Wicket","No Ball","Wide"]

import random
print("1st", f  ,random.choices(l2))
print("2nd", f  ,random.choices(l2))
print("3rd", f  ,random.choices(l2))
print("4th", f  ,random.choices(l2))
print("5th", f  ,random.choices(l2))
print("6th", f  ,random.choices(l2))
if l2 == "No Ball" or "Wide":
    print("Extra Ball", f ,random.choices(l2))


