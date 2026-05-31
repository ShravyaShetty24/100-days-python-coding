#Abstraction
class Phone:
    def call_contact(self,name):
        print(f"calling {name}...")
        print("call connected")
    def take_picture(self):
        print("opening camera")
        print("picture captured")
phone=Phone()
phone.call_contact("shravya")
phone.take_picture()
print()

#Inheritance
class Vehicle:
    def start(self):
        print("Vehicle strated")
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")
bike=Bike()
bike.start()
bike.ride()