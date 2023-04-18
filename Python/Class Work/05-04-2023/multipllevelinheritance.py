class a:
    def displaya(self):
        self.num1 = 10

class b:
    def displayb(self):
        self.num2 = 20

class c (a,b):
    def displayc(self):
        ans = self.num1 + self.num2
        print("Number 1  = ",self.num1)
        print("Number 2 = ",self.num2)

        print("ans = ",ans)


obj = c()
obj.displaya()
obj.displayb()
obj.displayc()