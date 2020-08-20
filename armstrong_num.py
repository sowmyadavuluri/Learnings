''' ARMSTRONG NUMBER : abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
Example:
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153'''

num = int(input("Enter a number: "))
sum = 0
y = num
while y>0:
    x = y % 10
    sum += x ** 3
    y //= 10
if num == sum:
   print("Num is an Armstrong")
else:
   print("Num is not Armstrong")


