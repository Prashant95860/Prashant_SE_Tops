class circle:
    r = int(input("Enter Radius : "))

    def area(self):
        a =  self.r**2*3.14
        print("Area of Circel : ",a)

    def perimeter(self):
        p = 2*self.r*3.14
        print("Perimeter of Circle : ",p)

obj = circle()
obj.area()
obj.perimeter()