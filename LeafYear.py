#Leaf year

a = 2000
if a % 400 == 0 and a % 100 == 0:
    print("Its leaf year")
elif a % 4 == 0 and a % 100 != 0:
    print("Its leaf year")
else:
    print("Its not leaf year")
