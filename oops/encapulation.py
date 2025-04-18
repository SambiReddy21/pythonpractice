"""
Strong Understanding of Python OOPs Concepts with Examples & Interview Questions
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which can contain data (attributes) and methods (functions). Python supports OOP with four main pillars:

Encapsulation
Abstraction
Inheritance
Polymorphism
1. Encapsulation
Encapsulation is the process of wrapping data (variables) and methods (functions) into a single unit (class). It helps in restricting direct access to variables and allows controlled access via methods.

Example of Encapsulation


"""

class Bankaccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depostied {amount}, New Balance:{self.balance}")
        else:
            print("Invalide amount!")
    
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdrawn{amount}, New Balance:{self.balance}")
        else:
            print("Insufficent funds!")
            
    def get_balance(self):
        return self.balance
    
account = Bankaccount("12345678", 2000)
account.deposit (4000)
account.withdraw (5000)
print(account.get_balance())

#🔹 Key Takeaway: The __balance attribute is private and can only be accessed via methods.


class Person:
    
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print('Hello, my name is', self. name)
                
p1 = Person('Abhi')
p2 = Person('Raju')
p1.say_hi()
p2.say_hi()
            
"""
2. Abstraction
Abstraction hides implementation details and only exposes essential functionalities. It is achieved using abstract classes in Python (ABC module).

Example of Abstraction

"""    

  