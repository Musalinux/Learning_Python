"""
Try writing a simple program following these concepts:

🔹 Create a class Employee with attributes name and salary.
🔹 Create a subclass Manager that inherits from Employee and adds a team_size attribute.
🔹 Use encapsulation to protect salary.
🔹 Use polymorphism for a method work(), where Manager and Employee have different implementations.
"""

# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public Attribute
        self._salary = salary  # Protected Attribute (Encapsulation)

    def work(self):  # Polymorphic method
        print(f"{self.name} is an Employee of JPMC.")

# Child Class (Inherits from Employee)
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Inherit attributes from Employee
        self.team_size = team_size  # New Attribute for Manager

    def work(self):  # Overriding the work method (Polymorphism)
        print(f"{self.name} is a Manager handling a team of {self.team_size} people.")

# Creating Objects
sam = Manager("Sam", 80000, 10)  # Manager with team size 10
tom = Employee("Tom", 50000)  # Regular Employee

# Calling Methods
sam.work()  # Output: Sam is a Manager handling a team of 10 people.
tom.work()  # Output: Tom is an Employee of JPMC.
