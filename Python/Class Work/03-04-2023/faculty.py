class faculty:
    def setid(self,id):
        self.id = id
    def getid(self):
        return self.id

    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name

    def settechonology(self,technology):
        self.technology = technology
    def gettechnology (self):
        return self.technology

obj = faculty()

id = int(input("Enter Id : "))
obj.setid(id)

name = input("Enter Your Name : ")
obj.setname(name)

technology = input("Enter Technology : ")
obj.settechonology(technology)

print(obj.getname())
print(obj.gettechnology())