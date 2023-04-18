# keyword : A word which have predefined meaning

            # A reserve word
            # you can not use as variable
"""
for
while
break
continue are example of keywords
"""

# through this programme you fetch keyword from user

import keyword
keyword_list = keyword.kwlist

name = input("Enter Name : ")

if name in keyword_list:
    print("Yes, It is Keyword")
else:
    print("No,It is not keyword")

# through this programme you fetch all the keywords
import keyword
keyword_list = keyword.kwlist
print(keyword_list)