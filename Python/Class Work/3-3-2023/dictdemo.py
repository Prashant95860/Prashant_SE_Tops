student = {
    #key      values
    "name" : "prashant",
    "subject" : "python",
    "marks" : 89
    }
print(student)
# if particulary value access in dictionary than enter key and it will be print value of key.

print(student["name"])

# it will print not in curely bracket it will print in seprate line.

for k,v in student.items():

    print(f"{k} = {v}")
    
# it will print only keys.

for k in student.keys():
    print(k)

# it will print only values.

for k in student.values():
    print(k)
