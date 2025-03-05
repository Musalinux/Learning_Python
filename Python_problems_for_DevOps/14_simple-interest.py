"""
Simple Interest = (P x T x R) / 100
Where,
P = Principle Amount
R = Rate
T = Time
"""

def simple_interest (principle, time, rate):
    p = principle
    t = time
    r = rate 
    
    simpleInterest = (p * r * t) / 100
    return simpleInterest
    
principle = int(input("Enter the priinciple amount: \n"))
time = int(input("Enter the time: \n"))
rate = int(input("Enter the rate: \n"))

simple_interest (principle, time, rate)
print (f"Simple interest is {simple_interest (principle, time, rate)}")