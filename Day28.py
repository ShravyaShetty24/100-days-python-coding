#create class
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("price:",self.price)
mobile1=Mobile("Samsung",250000)
mobile2=Mobile("Apple",700000)
mobile1.display()
print()
mobile2.display()
print()

#Method Definition
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
s1=Student("shravya",95)
s2=Student("sanvi",85)
s3=Student("khushi",91)
s1.display_info()
print()
s2.display_info()
print()
s3.display_info()