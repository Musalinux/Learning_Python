"""
Solid Principles
S - Single Repository Principle (SRP)
O - Open/Close Principle (OCP)
L - Liskov Substitution Principle (LSP)
I - Interface Segragation Principle (ICP)
D - Dependency Inversion Principle (DIP)
"""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    I - Interface Segragation Principle (ICP)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 💡 A class should only implement methods it actually uses.

### Bad Example (Violating ISP):
class Machine:
    def print(self):
        pass
    def scan(self):
        pass
    def fax(self):
        pass

class Printer(Machine):
    def print(self):
        print("Printing...")

    def scan(self):
        raise NotImplementedError("This printer cannot scan")  # ❌ Not needed

    def fax(self):
        raise NotImplementedError("This printer cannot fax")  # ❌ Not needed

# Problem: A basic printer shouldn't have scan or fax methods. 

# ✅ Fixed Example (Following ISP - Separate Classes for Different Functions):
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class FaxMachine:
    def fax(self):
        pass

class BasicPrinter(Printer):
    def print(self):
        print("Printing...")  # ✅ Only prints

class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print(self):
        print("Printing...")
    def scan(self):
        print("Scanning...")
    def fax(self):
        print("Faxing...")
        
"""        
📌 Why is this better?

A basic printer only prints.
A multi-function printer can print, scan, and fax without unused methods.
""" 