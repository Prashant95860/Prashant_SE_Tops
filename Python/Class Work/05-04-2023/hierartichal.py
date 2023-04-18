class rbi:
    def displayr(self):
        print("RBI IS PARENT CLASS")

class sbi (rbi):
    def displays(self):
        print("SBI IS CHILD CLASS")

class boi (rbi):
    def displayb(self):
        print("BOI IS CHILD CLASS")

obj = sbi()
obj.displayr()
obj.displays()

obj1 = boi()
obj1.displayr()
obj1.displayb()
