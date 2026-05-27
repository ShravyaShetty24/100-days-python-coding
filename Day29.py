class Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def display(self):
        print("movie name:",self.title)
        print("rating:",self.rating)
m1=Movie("toxic",10)
m2=Movie("kantara",9.9)
m1.display()
print()
m2.display()
print()

class Employee:
    def __init__(self,name,designation,salary=300000):
        self.name=name
        self.designation=designation
        self.salary=salary
    def dispaly(self):
        print("name:",self.name)
        print("designation:",self.designation)
        print("salary:",self.salary)
e1=Employee("shravya","software developer")
e2=Employee("sanvi","cyber")
e3=Employee("khushi","cloud computing")
e1.dispaly()
e2.dispaly()
e3.dispaly()