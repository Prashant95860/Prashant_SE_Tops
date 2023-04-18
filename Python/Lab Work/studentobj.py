class student:
    db = {}

    def input(self):
        email = input("email : ")
        password = input("password : ")

        self.db[email] = password

    def display(self):
        for k in self.db.keys():
            print("email = ",k)

obj = student()

status = True
while status:
    data = """
    
            press 1 for registration
            press 2 for faculty registration
            press 3 for exit
    
    """ 
    print(data)
    user = int(input("Enter Your Choice : "))
    if user == 1:
        obj.input()
    if user ==2:
        print("Faculty")
    else:
        status = False

choice = input ("Do you want more operation : ")
if choice == "n" or "N":
    status = False

    