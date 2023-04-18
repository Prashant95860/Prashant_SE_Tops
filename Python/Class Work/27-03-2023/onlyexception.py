# it only show the main error
try:
    print(a)
except Exception as e:
    print(e)



# import handling block
import sys

# exception handling block
try:
    print(a)

except:
    print("subject = ",sys.exc_info()[0])
    print("message = ",sys.exc_info()[1])
