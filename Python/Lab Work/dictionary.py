student = {
    'name' : 'Prashant',
    'student' : 'Python',
    'marks' : 85
    }
print(student)

print(student['name'])

for k,v in student.items():
    print(f"{k} = {v}")

for k in student.keys():
    print(k)

for k in student.values():
    print(k)
