class student:
    # setter methid
    def setid(self,id):
        self.id = id

    #getter method
    def getid(self):
        return self.id

    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name

obj = student()

# set data
id = int(input("Enter Id : "))
obj.setid(id)
name = input("Enter Name : ")
obj.setname(name)

# get data
print(obj.getname())

