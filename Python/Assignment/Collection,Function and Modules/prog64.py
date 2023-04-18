from decimal import*
d = list(map(Decimal, "2.45 2.69 3.45 2.00".split()))
print("Maximum : ",max(d))
print("Minimum : ",min(d))