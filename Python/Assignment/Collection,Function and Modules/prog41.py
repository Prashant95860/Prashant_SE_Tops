d = [{"p" : 1},{"p" : 1},{"r" : 2},{"s" : 3},{"h" : 3}]
u = set(val for dic in d for val in dic.values())
print("Unique Values :",u)