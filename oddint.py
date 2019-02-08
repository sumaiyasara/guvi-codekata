lower_limit, upper_limit = input().split()
lower_limit= int(lower_limit)
upper_limit= int(upper_limit)
for i in range(lower_limit+1,upper_limit):
  if(i%2 != 0):
    print(i,end=" ")
