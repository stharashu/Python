from abc import ABC

class Shape:
    def area(self):
        raise NotImplementedError()

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        # print(f"Enter the width and height: {width}")
        return self.width*self.height


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius ** 2
    