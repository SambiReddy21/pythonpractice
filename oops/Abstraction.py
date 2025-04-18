"""
2. Abstraction
Abstraction hides implementation details and only exposes essential functionalities. It is achieved using abstract classes in Python (ABC module).

Example of Abstraction

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass   #abstract Method
    
class Car(Vehicle):
    def start(self):
        print("Car engine started!")
    
class Bike(Vehicle):
    def start(self):
        print("Bike engine started!")
        
        
car = Car()
car.start()

bike = Bike()
bike.start()

# Key Takeaway: Vehicle is an abstract class that defines an interface but does not implement it. Subclasses must implement the start() method.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hi(self):
        print(f"Hi, my name is {self.name} and I am  {self.age} years of old.")
        
person1 = Person("John", 30)
person1.say_hi()        
