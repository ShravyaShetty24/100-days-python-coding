class account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0  #encapsulation

    def check_balance(self):
        print(f"balance is{self._balance}")

    def deposite(self,amount):
        self._balance+=amount
        print(f"deposite succesfull,updated balance{self._balance}")

    def withdrwal(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"withdrwal successfull,updated balnace{self._balance}")
        else:
            print("insuficient balance")


class savingsAccount(account):
    def calculate_interest(self):
        INTREST_RATE=0.04
        intrest=self._balance*INTREST_RATE
        print(f"intrest:{intrest}")

class currentAccount(account):
    def withdrwal(self, amount):
        overdraft_limit=1000
        if self._balance + overdraft_limit >= amount:
            self._balance-=amount
            print(f"withdrwal successfull,upadated balance{self._balance}")
        else:
            print("insuffieint balance")


class bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__accounts={}

    def create_account(self,id,holder_name,type):
        if type=="savingsAccount":
            new_account=savingsAccount(id,holder_name)
        elif type=="currentAccount":
            new_account=currentAccount(id,holder_name)
        else:
            print("invalid type")
            return None
        self.__accounts[id]=new_account
        print("account creation sucssfull")
        return new_account
    
    def get_account(self,id):
        if id not in self.__accounts:
            print("Account not found")
            return None
        else:
            account=self.__accounts[id]
            print(f"\nID{account.id}\nname{account.holder_name}")
            return account
        
ssb=bank("shravya shetty bank","Thirthahalli")
s1=ssb.create_account("1","sanvi","savingsAccount")
c1=ssb.create_account("2","khushi","currentAccount")
s1.deposite(1000)
c1.deposite(10)
s1.withdrwal(2000)
c1.withdrwal(20)
s1.calculate_interest()