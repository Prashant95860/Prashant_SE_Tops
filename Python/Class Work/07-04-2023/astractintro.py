from abc import ABC,abstractmethod

# inheritance ABC - Abstract Base Class

class Rbi(ABC):
    def roi(self):
        pass

class Sbi(Rbi):
    def roi(self):
        return 8.5
    
class Boi(Rbi):
    def roi(self):
        return 8.0
    
obj = Sbi()
print(obj.roi())

obj1 = Boi()
print(obj1.roi())

