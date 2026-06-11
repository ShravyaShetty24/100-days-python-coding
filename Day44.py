#method overriding

class Shape:
    def draw(self):
        print("drawing shape")
class Circle(Shape):
    def draw(self):
        super().draw
        print("drawing circle")
s=Shape()
c=Circle()
s.draw()
c.draw()

#abstract classes
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def __init__(self,hours,rate):
        self.hours=hours
        self.rate=rate
    def calculate_salary(self):
        return self.hours*self.rate
m=Manager(40,500)
print("salary=",m.calculate_salary())