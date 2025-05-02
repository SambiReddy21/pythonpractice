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




"""
What is Inheritance?
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class (child class) to inherit properties and behaviors (methods) from another class (parent class).

Why Use Inheritance?
✔ Code Reusability – Avoids redundant code.
✔ Extensibility – Easily modify or extend functionalities.
✔ Maintainability – Improves organization of code.

Types of Inheritance in Python
Single Inheritance

Multiple Inheritance

Multilevel Inheritance

Hierarchical Inheritance

Hybrid Inheritance


"""

#Single Inheritance
#A child class inherits from a single parent class.

# Parent Class
class Animal:
    def speak(self):
        return "I make a sound"

# Child Class
class Dog(Animal):
    def speak(self):
        return "Bark"

# Create an object of Dog
d = Dog()
print(d.speak())  # Output: Bark



#Multiple Inheritance
#A child class inherits from multiple parent classes.


# Parent Class 1
class Father:
    def show_father_traits(self):
        return "Father's traits"

# Parent Class 2
class Mother:
    def show_mother_traits(self):
        return "Mother's traits"

# Child Class
class Child(Father, Mother):
    def show_child_traits(self):
        return "Child's traits"

# Create object of Child
c = Child()
print(c.show_father_traits())  # Output: Father's traits
print(c.show_mother_traits())  # Output: Mother's traits
print(c.show_child_traits())   # Output: Child's traits