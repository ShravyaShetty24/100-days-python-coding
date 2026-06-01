#polymorphism
import math
class shape:
    def calculate_area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius*self.radius
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width
c=circle(5)
r=rectangle(4,6)
print("calculate area of circle:",c.calculate_area())
print("calculate area of rectangle:",r.calculate_area())