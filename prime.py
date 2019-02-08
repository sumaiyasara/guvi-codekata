b=int(input())
p=0
for i in range(2,b//2+1):
    if(b%i==0):
        p=p+1
if(p<=0):
    print("yes")
else:
    print("no")
