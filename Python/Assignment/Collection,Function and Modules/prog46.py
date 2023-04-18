from collections import Counter
l = [{"item": "item1","amount" : 400},{"item":"item2","amount" : 300},{"item" : "item1","amount" : 750}]
r = Counter()
for d in l:
    r[d["item"]] += d["amount"]
    print(r)