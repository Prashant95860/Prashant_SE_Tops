class grandparent():
    def land(self):
        print("Land in Gujarat")

class parent(grandparent):
    def house(self):
        print("House in Ahmedabad")

class child(parent):
    def car(self):
        print("I have car")


obj = child()

obj.land()
obj.house()
obj.car()
    