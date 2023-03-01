l = ["Python",1,2,1.1,1.2,0,0,True,False,"Python Programming"]
print(l)

#"append" : it is use for add value in last.
l.append(100)
print(l)

#"copy" : is used for copy the list.
l1 = l.copy()
print(l1)

l1.append(200)
print(l1)

#"count" : something in list use "count".
print(l.count(0))
print(l.count(1))

#pop is used for remove last value from list
l.pop()
print(l)
l.pop()
print(l)

# "extend" : is used for add the more than one value

l3 = [1001,1002,1003]
l.extend(l3)
print(l)

#"index" : is used for find index of particular index
print(l.index(1003))

#insert : is used for enter element in particullar index
l.insert(2,"Shukla")
print(l)

#remove : is used for any remove any value.
l.remove(1.1)
print(l)

#reverse : is used for print reverse list.
l.reverse()
print(l)

#show list in indivisully use loop.

for i in l:
    print(i)
















