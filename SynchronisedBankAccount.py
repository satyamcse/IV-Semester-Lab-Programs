from threading import Lock
import threading
print("Hello World")
class BankAc:
    def __init__(self,name):
        self.lock = Lock()
        self.name = name
        self.balance = 0
    def deposit(self,amount):
        with(self.lock):
            for i in range(amount):
                self.balance+=1
            print("New Balance after deposit = ",self.balance)
    def withdraw(self,amount):
        with(self.lock):
            for j in range(amount):
                self.balance-=1
            print("New Balance after withdraw = ",self.balance)
def t1():
    for i in range(10000):
        satyam.withdraw(500)
def t2():
    for i in range(10500):
        satyam.deposit(500)
satyam = BankAc("Satyam")
t1 = threading.Thread(target=t1) 
t2 = threading.Thread(target=t2) 
t2.start()
t1.start() 
