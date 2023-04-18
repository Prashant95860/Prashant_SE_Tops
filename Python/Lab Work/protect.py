class product:
    def __init__(self):
        self.__mobile = 15000 # private
        self.laptop = 25000

    def display(self):
        print("mobile", self.__mobile)
        print("laptop", self.laptop)

    # data change method
    def change(self,new):
        self.__mobile = new

# object
obj = product()
obj.display()

# change price
obj.mobile = 18000
obj.laptop = 35000
obj.display()

obj.change(19000)
obj.display()


     