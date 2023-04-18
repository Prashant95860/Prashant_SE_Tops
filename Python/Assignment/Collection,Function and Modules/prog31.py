d = {"c" : 3,"b" : 2,"d" : 4,"a" : 1}

sort = sorted([(value, key) for (key,value) in d.items()])

print("Sorted dictionary is : ",sort)