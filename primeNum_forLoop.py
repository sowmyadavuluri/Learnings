#Python program to print all Prime numbers in an Interval
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

for val in range(start,end+1):
   if val >1 :
      for n in range(2, val//2 +2):
         if val % n == 0:
              if val == n:
                 print(val) 
              else: break
           
         else :
           print(val)
 
     
