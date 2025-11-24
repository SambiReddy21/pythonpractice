"""
OOPs Concepts in Python
Python supports 4 main OOP principles:

1. ✅ Class & Object
Class = Blueprint/template

Object = Instance of class
"""
class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        
router = Device("Router1", "192.168.1.1")
print(router.name, router.ip)

"""
2. 🔒 Encapsulation
Binding data and methods into one unit (class)

Protecting data with private attributes

"""

class Device:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name




#child class inherits properties of parent class

class NetworkDevice:
    def __init__(self, ip):
        self.ip = ip
        

class Router(NetworkDevice):
    def display(self):
        print(f"Router IP: {self.ip}")

r1 = Router("10.1.1.1")
r1.display()



"""
4. 🔁 Polymorphism
Same function/method behaves differently depending on the object

"""

class Switch:
    def connect(self):
        print("Connecting to Switch")
        
class Firewall:
    def connect(self):
        print("Connecting to Firewall")
        
for device in (Switch(), Firewall()):
    device.connect()
    
    