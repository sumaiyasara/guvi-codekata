p=int(input())
c=list(map(int,str(p)))
d=list(map(lambda x:x**3,c))
if(sum(d)==p):
    print("yes")
else:
    print("no")
