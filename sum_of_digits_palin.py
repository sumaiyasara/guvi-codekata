n=int(input())
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
temp=tot
rev=0
while(tot>0):
    dig=tot%10
    rev=rev*10+dig
    tot=tot//10
if(temp==rev):
    print("YES")
else:
    print("NO")
