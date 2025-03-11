"""
Solid Principles
S - Single Repository Principle (SRP)
O - Open/Close Principle (OCP)
L - Liskov Substitution Principle (LSP)
I - Interface Segragation Principle (ICP)
D - Dependency Inversion Principle (DIP)
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    S - Single Repository Principle (SRP) 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 💡 Each function/class should do only one thing.

### Bad Example (Violating SRP): 
class Report:
    def generate(self):
        print("Generating report...")

    def save_to_file(self):
        print("Saving report to file...")  # ❌ File saving is a different responsibility

    def send_email(self):
        print("Sending report via email...")  # ❌ Emailing is another responsibility

### Good Example following SRP:
class ReportGenerator:
    def generate(self):
        print("Generating report...")

class FileSaver:
    def save(self):
        print("Saving report to file...")

class EmailSender:
    def send(self):
        print("Sending report via email...")

report = ReportGenerator()
report.generate()

file_saver = FileSaver()
file_saver.save()

email_sender = EmailSender()
email_sender.send()

"""
📌 Why is this better?

Each class does only one thing (Report, File Saving, Email Sending).
If we need to change how we save files, we don't touch the report generation.
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    O - Open/Close Principle (OCP)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 💡 You should be able to add new features without modifying old code. 

### Bad Example (Violating OCP):
class PaymentProcessor:
    def process_payment(self, method):
        if method == "credit_card":
            print("Processing credit card payment...")
        elif method == "paypal":
            print("Processing PayPal payment...")
        else:
            print("Payment method not supported!")  # ❌ Every time we add a new method, we modify this class.

### Fixed Example (Following OCP - Using Functions for Extension):
class PaymentProcessor:
    def process_payment(self):
        pass  # Empty function, will be defined in child classes

class CreditCardPayment(PaymentProcessor):
    def process_payment(self):
        print("Processing credit card payment...")

class PayPalPayment(PaymentProcessor):
    def process_payment(self):
        print("Processing PayPal payment...")

def execute_payment(payment):
    payment.process_payment()

credit_card = CreditCardPayment()
paypal = PayPalPayment()

execute_payment(credit_card)
execute_payment(paypal)

"""
📌 Why is this better?

If we add a new payment method, we don't modify the old code—we just create a new class.
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    L - Liskov Substitution Principle (LSP)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    D - Dependency Inversion Principle (DIP)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 💡 High-level modules should not depend on low-level modules. Both should depend on abstractions.

### Bad Example (Violating DIP):
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL database")

class App:
    def __init__(self):
        self.db = MySQLDatabase()  # ❌ If we switch to PostgreSQL, we must change this

# 🚨 Problem: The App is tightly coupled to MySQLDatabase.

### ✅ Fixed Example (Following DIP - Use Dependency Injection):
class Database:
    def connect(self):
        pass  # Empty function, will be defined in child classes

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database")

class App:
    def __init__(self, db: Database):  # ✅ Inject dependency
        self.db = db

    def start(self):
        self.db.connect()

app1 = App(MySQLDatabase())  # ✅ Works with MySQL
app1.start()

app2 = App(PostgreSQLDatabase())  # ✅ Works with PostgreSQL
app2.start()

"""
📌 Why is this better?

App now works with any database (MySQL, PostgreSQL, etc.) without modifying its code.
It depends on an abstraction (Database), not a specific class.
"""