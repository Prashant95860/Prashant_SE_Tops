t = (10,20,30)
print(type(t))
print(t)

# if one element write down in typle it is not consider as tuple.

t = ("python")
print(type(t))

t= ("python",)

t = ("python","java","Android","Flutter","React")
print(t)
# loop is use for print in sequence and new line
for item in t:
    print(item)

t= ("python",)

t = ("python","java","Android","Flutter","React")
print(t)
# end parameter print values in horizontal line
for item in t:
    print(item,end=",")
    
    print(len(t))