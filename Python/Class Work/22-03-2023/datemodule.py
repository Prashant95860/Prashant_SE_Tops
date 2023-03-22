# date module
from datetime import date

mydate = date(2023,3,22)
print("date = ",mydate)

# current date

from datetime import date

current = date.today()

print("Current Date = ",current)

# only year fetch
print(current.year)
# only month fetch
print(current.month)
# only day fetch
print(current.day)


# time module

from datetime import time

t = time(10,20,30)
print(t)

