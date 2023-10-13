
#Palindrome

num = int(input("Enter the number: "))
val = str(num)
if val==val[::-1]:
    print("The number is palindrome ")
else:
    print("This is not a palindrome number ")
for i in range(10):
    if val.count(str(i))>0:
        print(str(i),"appears",val.count(str(i)),"Times")
