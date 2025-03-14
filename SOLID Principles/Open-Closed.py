"""
Solid Principles
S - Single Repository Principle (SRP)
O - Open/Close Principle (OCP)
L - Liskov Substitution Principle (LSP)
I - Interface Segragation Principle (ICP)
D - Dependency Inversion Principle (DIP)
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
