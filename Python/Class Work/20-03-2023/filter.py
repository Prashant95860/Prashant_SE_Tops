"""
l1 = ["a","e","j","k","o"]
vowel_list = ["a","e","i","o","u"]
l2 = []

def check():
    for c in l1:
        if c in vowel_list:
            l2.append(c)

check()
for i in l2:
    print(i)

    """

l1 = ["a","e","j","k","o"]
vowel_list = ["a","e","i","o","u"]

def myfun(seq):
    if (seq in vowel_list):
        return True
    else:
        return False
    
filter_data = filter(myfun,l1)

for i in filter_data:
    print(i)


    