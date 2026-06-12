class employee:
    def __init__(self):
        self.__salary=0
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def display(self):
        print("employee")
class manager(employee):
    def display(self):
        print("manager")
m=manager()
m.set_salary(50000)
m.display()
print("ssalary:",m.get_salary())