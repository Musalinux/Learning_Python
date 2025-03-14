"""
Solid Principles
S - Single Repository Principle (SRP)
O - Open/Close Principle (OCP)
L - Liskov Substitution Principle (LSP)
I - Interface Segragation Principle (ICP)
D - Dependency Inversion Principle (DIP)
"""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    L - Liskov Substitution Principle (LSP)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 💡 A subclass should work properly when used in place of its parent class.

### Bad Example (Violating LSP): 
class Bird:
    def fly(self):
        print("Flying...")

class Penguin(Bird):  
    def fly(self):
        print("Penguins can't fly!")  # ❌ Penguins shouldn't have a fly method

# Problem: If we expect Bird.fly(), a penguin shouldn't break the behavior. 


### Fixed Example (Following LSP - Separate Classes for Flying & Non-Flying Birds):
class Bird:
    def make_sound(self):
        print("Bird is making a sound")

class FlyingBird(Bird):
    def fly(self):
        print("Flying high!")

class Sparrow(FlyingBird):
    pass  # Sparrow can fly

class Penguin(Bird):
    pass  # Penguin doesn't have a fly method

# Using the classes
sparrow = Sparrow()
sparrow.fly()  # ✅ Works

penguin = Penguin()
# penguin.fly()  ❌ This won't exist anymore (fixed the issue)
"""
📌 Why is this better?
Penguin doesn't have a .fly() method because it shouldn't.
Sparrow inherits flying behavior correctly.
"""