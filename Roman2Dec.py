
#Convertion of roman to decimal

def roman2dec(romastr):
    roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':100}
    romanBack = list(romastr)[::-1]
    value = 0

    rightVal = roman_dict[romanBack[0]]
    for numeral in romanBack:
        leftVal = roman_dict[numeral]

        if leftVal<rightVal:
            value -= leftVal
        else:
            value += leftVal
        rightVal = leftVal
    return value


romanStr = int(input("Enter roman number: "))
print(roman2dec(romanStr))

