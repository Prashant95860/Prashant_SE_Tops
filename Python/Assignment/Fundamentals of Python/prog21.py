s = input("Enter Word : ")
if len(s) % 4==0:
    print("".join(reversed(s)))
else:
    print(s)