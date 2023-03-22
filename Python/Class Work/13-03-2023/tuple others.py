t = ("python","java","Android","Flutter","React","java")
# it will print length of tuple
print(len(t))
#it will repeat tuple
print(t.count("java"))
# casting for change some value in tuple
l1 = list(t) # casting into list
l1[0] = "Flutter"
t = tuple(l1) #recasting into tuple 
print(t)
