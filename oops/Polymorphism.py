"""
4. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the same method name to have different implementations.

Example of Polymorphism


"""


class Bird:
    def fly(self):
        print("Some birds can fly, some cannot.")

class Sparrow(Bird):
    def fly(self):
        print('Sparrow can fly!')
        
class Penguin(Bird):
    def fly(self):
        print('Penguin cannot fly!')
        
birds = [Sparrow(), Penguin()]

for bird in birds:
    bird.fly()
    
#Key Takeaway: The fly() method is polymorphic, as its behavior changes based on the object calling it.
    
    