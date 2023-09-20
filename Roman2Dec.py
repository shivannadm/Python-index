
#Convertion of roman to decimal

def roman2dec(romastr):
    roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':100}
    romanBack = list(romastr)[::-1]
    value = 0

    rightval = roman_dict[romanBack[0]]
    for numeral in romanBack:
        leftval = roman_dict[numeral]

    if leftval<rightval:
        value -= leftval
    else:
        value += rightval
    return value


romanStr = int(input("Enter roman number: "))
print(roman2dec(romanStr))

