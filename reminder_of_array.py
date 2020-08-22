'''Find remainder of array multiplication divided by n:
Given multiple numbers and a number n, the task is to print the remainder after multiply all the number divide by n.

Examples:

Input : arr[] = {100, 10, 5, 25, 35, 14}, 
            n = 11
Output : 9
100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9'''


def mulp(arr,x,n):
   multp = 1
   for i in range(x):
     multp = (multp * (arr[i]%n))% n 
     
   return multp % n
arr = [100,10,5,25,35,14]
n = int(input("Enter the number:"))
x = len(arr)
print(mulp(arr,x,n))

