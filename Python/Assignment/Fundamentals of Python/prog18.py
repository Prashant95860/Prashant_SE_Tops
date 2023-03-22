s = input("Enter String : ")
s1 = input("Enter String : ")

if len(s) >2:
    if s.endswith("ing"):
        s += "ly"
    else:
        s += "ing"

if len(s1) >2:
    if s1.endswith("ing"):
        s1 += "ly"
    else:
        s1 += "ing"

print(s)
print(s1)