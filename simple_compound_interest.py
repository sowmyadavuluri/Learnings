'''simple interest formula is given by: Simple Interest = (P x T x R)/100
Where,P is the principle amount,T is the time and,R is the rate
nput : P = 10000 R = 5  T = 5
Output :2500
We need to find simple interest on Rs. 10,000 at the rate of 5% for 5 units of time.
ormula to calculate compound interest annually is given by:
compound interest :
A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount'''

p = int(input("enter the principal amount: "))
r = int(input("enter the rate: "))
t = int(input("enter the time: "))
s = (p*r*t)/100
a = (p*(1+ (r/100)))*t
print("Compound Interest is : ", a)
print("Simple Interest is : ", s)

