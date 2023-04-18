from abc import ABC,abstractmethod

class vehicle (ABC):
    def wheels(self):
        pass
    def color(self):
        pass

class car(vehicle):
    def wheels(self):
        return 4
    def color(self):
        return "red" 
    
class bike(vehicle):
    def wheels(self):
        return 2
    def color(self):
        return "blue"
    
class truck(vehicle):
    def wheels(self):
        return 8
    def color(self):
        return "green"
    
obj = bike()
print(obj.wheels())
print(obj.color())

obj1 = car()
print(obj1.color())
print(obj1.wheels())

obj2 = truck()
print(obj2.color())
print(obj2.wheels())
    
