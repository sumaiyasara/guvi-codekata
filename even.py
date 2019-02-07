while True:
	try:
		num=int(input(""))
		break
	except:
		print("invalid")
		break
if(num%2==0):
    print("Even")
else:
    print("Odd")
