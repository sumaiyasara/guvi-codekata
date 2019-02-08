str=input()
try:
    i = float(str)
    print("yes")
except (ValueError, TypeError):
    print("No")
