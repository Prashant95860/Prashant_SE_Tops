# single inheritance : one parent and one child

"""
class parent:
    def home(self):
        print("Ahmedabad")

class child(parent):
    def car(self):
        print("I HAVE CAR")

obj = child()
obj.home()
obj.car()
"""

"""
# multiple Inheritance : Grand parent,parent & child

class grandparent:
    def home(self):
        print("Ahmedabad")

class parent(grandparent):
    def car(self):
        print("I HAVE CAR")

class son(parent):
    def prop(self):
        print("I HAVE PROPERTY")

obj = son()
obj.home()
obj.car()
obj.prop()

"""
"""
# Multileve Inheriitance : One child & two parent
class dad:
    def d(self):
        print("I AM FATHER OF A")

class mom:
    def c(self):
        print("I AM MOTHER OF A")
class son (mom,dad):
    def a(self):
        print("i am son")

obj = son()
obj.d()
obj.c()
obj.a()

"""


# Hierartichal Ineheritance : One Parent & Two child

"""

class parent:
    def par(self):
        print("I AM PARENT OF A & B")

class child(parent):
    def ch(self):
        print("I AM CHILD A")

class childb(parent):
    def chb(self):
        print("I AM CHILD B")

obj = childb()
obj.par()
obj.chb()

obj1 = child()
obj1.par()
obj1.ch()
    """






