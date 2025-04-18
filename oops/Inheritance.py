"""
3. Inheritance
Inheritance allows one class (child) to acquire properties and behaviors of another class (parent). It promotes reusability.

Example of Inheritance

"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        print("Some generic sound")
    
class Dog(Animal):
    def make_sound(self):
        print(f"Bark! Bark!{self.name}")
        Animal.make_sound(self)

class Cat(Animal):
    def make_sound(self):
        print(f"Meow! {self.name}")
        Animal.make_sound(self)
        
dog = Dog("Buddy")
cat = Cat('Whiskers')

dog.make_sound()
cat.make_sound()


#🔹 Key Takeaway: Dog and Cat classes inherit from Animal and override the make_sound() method.


"""
 Key Takeaway: Dog and Cat classes inherit from Animal and override the make_sound() method.

Types of Inheritance
Single Inheritance – One child inherits from one parent.
Multiple Inheritance – A child inherits from multiple parents.
Multilevel Inheritance – A child inherits from another child class.
Hierarchical Inheritance – Multiple child classes inherit from a single parent.
Hybrid Inheritance – Combination of multiple inheritance types.


"""