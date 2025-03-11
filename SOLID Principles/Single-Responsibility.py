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