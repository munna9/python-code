class account(object):
    def __init__(self, holder, number, balance, creditline=1500):
           self.Holder = holder
           self.number = number
           self.balance = balance
           self.creditline = creditline
    def deposit(self,amount):
        self.amount = amount
    def withdraw(self,amount):
        if(self.balance - amount <- self.creditline):
            return False
        else:
            self.balance -= amountCan't login: Connect to munna:443 [munna/192.168.56.1, munna/10.1.10.98] failed: Connection refused: connect
    def balance(self):
        return True
    def transfer(self,target,amount):
        if(self.balance - amount <- self.creditline):
            return False
        else:
            self.balance -= amount
            self.target += amount
            return True