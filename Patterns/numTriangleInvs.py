# Revers Number triangle pattern

x = 6
for i in range(6):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,6):
        print(x,end=' ')
    for j in range(i,6-1):
        print(x,end=' ')
    x -= 1
    print()

    '''
    Output
  6 6 6 6 6 6 6 6 6 6 6 
    5 5 5 5 5 5 5 5 5        
      4 4 4 4 4 4 4
        3 3 3 3 3
          2 2 2
            1
    '''

# 

for i in range(6):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,6):
        print(i+1,end=' ')
    for j in range(i,6-1):
        print(i+1,end=' ')
    print()

    '''
    Output
  1 1 1 1 1 1 1 1 1 1 1      
    2 2 2 2 2 2 2 2 2        
      3 3 3 3 3 3 3
        4 4 4 4 4
          5 5 5
            6

    '''
