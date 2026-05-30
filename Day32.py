#Encapsulation
class BankAccount:
    def __init__(self,account_number,balance):
        self.__acount_number=account_number
        self.__balance=balance
    def check_balance(self):
        print("Balance",self.__balance)
    def deposit(self,amount):
        self.__balance+=amount
        print(amount,"deposited successfully")
    def withdrw(self,amount):
        if amount<+ self.__balance:
            self.__balance-= amount
            print(amount,"withdrawn successfully")
        else:
            print("Insuficient balance")
acc=BankAccount("12345",1000)
acc.check_balance()
acc.deposit(500)
acc.withdrw(300)
acc.check_balance()
acc.__balance