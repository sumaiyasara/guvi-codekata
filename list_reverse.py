while True:
	try:
		x=int(input())
		k=input().split()
		break
	except:
		print("Invalid input")
		break
if(len(k)==x):
	print('->'.join(str(x) for x in k[::-1]))
