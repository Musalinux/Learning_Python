"""
Compound Interest annually formula:
A = P x (1 + R / 100) ^ T
Compound Interest = A - P

Where,
A = Amount 
P = Principle Amount
R = Rate
T = Time span
"""

def compound_interest (principle, time, rate):
    p = principle
    t = time
    r = rate 
    
    a = p * (pow(1 + (r/100), t))  
    compound_interest = a - p 
    return compound_interest

principle = float(input("Enter the principle amount: \n"))
rate = float(input("Enter the rate: \n"))
time = float(input("Enter the time: \n"))

compound_interest (principle, time, rate)
print (f"Compound interest is {compound_interest (principle, time, rate)}")