# define class
class student:
    # setter method
    def setid(self,id):
        self.id = id
    # getter method
    def getid(self):
        return self.id
    
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    
# object of class student
obj = student()

# set data 
id = int(input("Enter Id : "))
obj.setid(id)
name = input("Enter Name : ")
obj.setname(name)

# print data
print(obj.getname())