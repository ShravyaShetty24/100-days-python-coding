# SOLID principle
#1.Single Responsibility Principle

class book:
   def __init__(self,title,author,price):
      self.title=title
      self.author=author
      self.price=price
class bookprinter:
   def printer_daetails(self,book):
      print("Book titlle:",book.title)
      print("author:",book.author)
      print("Price:",book.price)
book=book("python basics","shravya","500")
printer=bookprinter()
printer.printer_daetails(book)
print()

#2.Open closed Principle

class product:
   def __init__(self,price):
      self.price=price
   def calculate_tax(self):
      return 0
class Food(product):
   def calculate_tax(self):
      return self.price*0.05
class Electronics(product):
   def calculate_tax(self):
      return self.price*0.05
food=Food(1000)
tv=Electronics(200000)
print("Food tax:",food.calculate_tax())
print("Electronics tax:",tv.calculate_tax())