class Shape:
    def __init__(self):
        pass 

    def area(self):
        print("Area: 0")  


class Square(Shape):
    def __init__(self, length):
        self.length = length 

    def area(self):
        print(f"Area of Square: {self.length * self.length}") 


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length 
        self.width = width 

    def area(self):
        print(f"Area of Rectangle: {self.length * self.width}") 


square = Square(4)
square.area() 

rectangle = Rectangle(4, 5)
rectangle.area() 