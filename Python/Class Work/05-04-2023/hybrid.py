class parent:
    def a(self):
        print("A is parent class")

class parentb(parent):
    def b(self):
        print("B is child class of A")

class parentc(parent):
    def c(self):
        print("C is Child of A")

class parentd(parentb,parentc):
    def d(self):
        print("D is Child class of B & C ")

obj = parentd()
obj.b()
obj.c()
obj.d()

obj1 = parentb()
obj1.a()
obj1.b()

obj2 = parentc()
obj2.a()
obj2.c()