# Number Triangle (Right angle triangle mirror image)

x = 1
for i in range(6):
    for j in range(i,6):
        print(x,end=' ')
    x += 1
    print()

    '''
    Output
        1 1 1 1 1 1 
        2 2 2 2 2
        3 3 3 3
        4 4 4
        5 5
        6

    '''

for i in range(6):
    for j in range(i,6):
        print(i+1,end=' ')
    print()

    '''
    Output
        1 1 1 1 1 1 
        2 2 2 2 2
        3 3 3 3
        4 4 4
        5 5
        6

    '''


p = 1
for i in range(6):
    for j in range(i,6):
        print(p,end=' ')
        p += 1
    print()

    '''
     Output   
        1 2 3 4 5 6
        7 8 9 10 11
        12 13 14 15
        16 17 18
        19 20
        21
    '''
