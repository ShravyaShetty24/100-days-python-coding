#getter and setter
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance>0:
            self.__balance=balance
        else:
            print("zero balance")
b=BankAccount(1000)
print(b.get_balance())
b.set_balance(100)
print(b.get_balance())

#Mthod overloading
class Calculator:
    def mul(self,a,b,c=1):
        return (a*b*c)
c=Calculator()
print(c.mul(2,3))
print(c.mul(4,5,2))