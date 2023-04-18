class product:
    #constructor
    def __init__(self):
        self.__mobile = 15000 # private
        self.laptop = 25000

    
    # display method
    def display(self):
        print("mobile ",self.__mobile)
        print("laptop",self.laptop)
    # data change method
    def changedata(self,newprice):
        self.__mobile = newprice

# object
obj = product()
obj.display()

# change mobile and laptop price
obj.__mobile = 18000
obj.laptop = 35000

obj.display()

# change mobile and laptop price
print("Change data using method")

obj.changedata(19000)
obj.display()


