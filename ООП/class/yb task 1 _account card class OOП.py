from datetime import datetime as dt
import pytz


# init
# color
GREEN = '\033[0;92m'
RED = '\033[1;31m'
WHITE = '\033[00m'

class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []
        
    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append(
            [amount, pytz.utc.localize(
            dt.utcnow())])
        
    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
            print(f'we spend {amount} money')
            self.show_balance()
            self.history.append(
            [-amount, pytz.utc.localize(
            dt.utcnow())])
        else:
            print('not enough money')
            self.show_balance()
        
    def show_balance(self):
        print(f'balance: {self.balance}')
        
    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction ='deposited' #text = str
                color = GREEN
            else:
                transaction = 'withdraw' #text = str
                color = RED
            #здесь конструктором собираем все что хотим show 
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')
            
        
a = Account()
