
# class define for student
class student:
    # dictionary - we use as a database
    db = {}

    # input method - which accept value from student user

    def input(self): # self keyword which is used to accesss inside class properties

        email = input("Enter email : ")
        password = input("Enter Password : ")

        # storing data in db
        # here email is key value is password
        self.db[email] = password

    def display(self):
        # display all students
        for k in self.db.keys():
            print("email = ",k)

# object creation of student class
s = student()
status = True
while status:
   


    
# menu
    data = """
        press 1 for student registration
        press 2 for faculty registration
        press 3 for view all students
        press 4 for exit

"""
    print(data)
    user = int(input("Enter your choice : "))
    if user ==1:
        s.input()
    elif user ==2:
        print("Faculty Input")
    elif user ==3:
        s.display()
    else:
        status = False

choice = input("do you want to perform more operations : ")
if choice == "n":
    status = False