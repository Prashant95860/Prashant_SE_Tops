
"""

ans = lambda n1,n2: n1+n2
print(ans(10,20))




l1 = ["a","e","f","h","i"]
vowl = ["a","e","i","o","u"]

def myfun(vow):
    if (vow in vowl):
        return True
    else:
       return False

filter_data = filter(myfun,l1)

for i in filter_data:
    print(i)




data = [2,8,12,18,25,30,22]
def myfun(even):
    if even%2==0:
        return True
    else:
        return False
    
filter_data = filter(myfun,data)
for i in filter_data:
    print(i)

    """

s = ["java","python","android","math","english"]
tops = ["java","python"]

def myfun(seq):
        if seq in tops:
            return True
        else:
            return False
        
filter_data = filter(myfun,s)
for i in filter_data:
        print(i)






















