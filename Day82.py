#3.Liskov Substitution Principle

class Vehicle:
   def move(self):
      print("Vehicle is moved")
class car(Vehicle):
   def move(self):
      print("car is moving on the road")
class boat(Vehicle):
   def move(self):
      print("boat is sailing on water")
Vehicles=[car(),boat()]
for v in Vehicles:
   v.move()
print()

#4.Dependency Inversion Principle

from abc import ABC,abstractmethod
class Appliance(ABC):
   @abstractmethod
   def turn_on(self):
      pass
class Fan(Appliance):
   def turn_on(self):
      print("Fan is on")
class AC(Appliance):
   def turn_on(self):
      print("AC is on")
class Remote:
   def __init__(self,appliance):
      self.appliance=appliance
   def press_button(self):
      self.appliance.turn_on()
fan=Fan()
ac=AC()
remote1=Remote(fan)
remote2=Remote(ac)
remote1.press_button()
remote2.press_button()