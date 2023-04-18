# class creation
class parent:
    def home(self): # define method
        print("Ahmedabad")

class child(parent): # in bracket use parent class name it represent as inheritance
    def car(self):
        print("I have car")

# object creation object only create child class
obj = child()
obj.home()
obj.car()

# through inheritance we create multiple class and through one object we access all the class.

