"""
Solid Principles
S - Single Repository Principle (SRP)
O - Open/Close Principle (OCP)
L - Liskov Substitution Principle (LSP)
I - Interface Segragation Principle (ICP)
D - Dependency Inversion Principle (DIP)
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