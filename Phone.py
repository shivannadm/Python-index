import re

def isphonenumber(num):
    if len(num) != 12:
        return False
    for i in range(len(num)):
        if i==3 or i==7:
            if num[i] != "-":
                return False
        else:
            if num[i].isdigit() == False:
                return False
    return True

def chkphonenumber(num):
    ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match(num):
        return True
    else:
        return False

ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using Regular Expression")
if chkphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")