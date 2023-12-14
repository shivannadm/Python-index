# Number right angle triangle

for i in range(6):
    for j in range(i+1):
        print(i+1,end=' ')
    print()
print("\n")

'''
    Output
        1) ⬇️
         1 
         2 2
         3 3 3
         4 4 4 4
         5 5 5 5 5
         6 6 6 6 6 6

    '''

p=1
for i in range(6):
    for j in range(i+1):
        print(p,end=' ')
    p=p+1
    print()
print("\n")

'''
    Output 
         2) ⬇️
         1
         2 2
         3 3 3
         4 4 4 4
         5 5 5 5 5
         6 6 6 6 6 6
    '''

# Contineous number pattern
x=1
for i in range(6):
    for j in range(i+1):
        print(x,end=' ')
        x=x+1
    print()

    '''
        Output
         3) ⬇️
         1
         2 3
         4 5 6
         7 8 9 10
         11 12 13 14 15
         16 17 18 19 20 21

     '''
