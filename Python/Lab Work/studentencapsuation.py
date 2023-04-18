class faculty:
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    
    def settech(self,tech):
        self.tech = tech
    def gettech (self):
        return self.gettech
    
obj = faculty()
name = input("Enter Name : ")
obj.setname(name)
tech = input("Enter Technology : ")
obj.settech(tech)

print(obj.getname())