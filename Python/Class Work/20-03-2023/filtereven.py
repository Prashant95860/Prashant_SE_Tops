data_set = [12,20,40,30,8,12]

def myfun(data):
    if data%2 ==0:
        return True
    else:
        return False
    
filter_data = filter(myfun,data_set)
for i in filter_data:
    print(i)