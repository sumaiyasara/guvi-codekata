def factors(k):
   for i in range(1, k + 1):
       if i%2 != 0:
         if k%i == 0:
           print(i)
n=int(input())
factors(n)
