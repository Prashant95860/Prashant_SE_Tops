"""
*args : arguments (tuple as parameter)

**kwrgs :key with arguments (dictionary as parsmeter)


"""

# normal function with normal parameter 

def sum(n1,n2):
    ans = n1+n2
    print(ans)

sum(10,20) 

# args function (tuple as parameter)
def add(*n):
    ans = 0
    for i in n:
        ans += i
    print(ans)

add(20,50,80,100,220)


# kwrgs fuction (dictionary as parameter)
def myfun(**kwrgs):
    for k,v in kwrgs.items():
        print(f"{k} = {v}")


myfun(name="Anjali",sub="python")