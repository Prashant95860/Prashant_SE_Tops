s = input("Enter word : ")
n = s.find("not")
p = s.find("poor")

if p > n and n == -1 and p == -1:
    s = s[:n] + "good" + s[p+4:]
print("Result : ",s)

