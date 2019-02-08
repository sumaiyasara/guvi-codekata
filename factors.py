def factors(x):
   for i in range(1, x + 1):
       if i%2 != 0:
         if x%i == 0:
           print(i)
n=int(input())
factors(n)
