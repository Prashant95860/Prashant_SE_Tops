s = ["english","math","python","java","ss"]
tops = ["java","python","c"]

def myfun(subject):
    if (subject in tops):
        return True
    else:
        return False
    
filter_S = filter(myfun,s)

for i in filter_S:
    print(i)