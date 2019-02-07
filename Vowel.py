while True:
	try:
		ch=input("")
		break
	except:
		print("invalid")
		break
if(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("Vowel")
else:
    print("Consonant")
