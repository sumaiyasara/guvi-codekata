m = int(input())
d=0
for i in range(1,m):
  for j in range(i,m+1):
    if(i!=j):
      d+=1
print(d)
