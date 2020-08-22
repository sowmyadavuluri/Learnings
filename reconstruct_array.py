'''Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M
The elements in the orginal array are related as, for every index i, a[i] = (a[i-1]+1)% M.

It is guaranteed that there is one non zero value in the array.

Examples:

Input: arr[] = {5, -1, -1, 1, 2, 3}, M = 7
Output: 5 6 0 1 2 3
M = 7, so value at index 2 should be (5+1) % 7 = 6
value at index 3 should be (6+1) % 7 = 0
'''
  
def result(a,n,m):
   index = 0

   for i in range(n):
       if (a[i]!=-1):
          index  = i
          break
   for i in range(index-1,-1,-1):
       if (a[i]==-1):
           a[i]=(a[i+1]-1+m)% m 
   for i in range(index +1, n):
       if(a[i]==-1):
            a[i] =(a[i-1]+1)% m  
   print(*a)
a = [5, -1, -1, 1, 2, 3]
m = int(input("Enter  m: "))
n = int(input("Enter  n: "))
result(a,n,m)

