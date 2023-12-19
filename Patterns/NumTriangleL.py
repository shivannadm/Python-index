#Left angle Triangle (in numbers)

x = 6
for i in range(6):
    for j in range(i,6):
        print(" ",end=' ')
    for j in range(i+1):
        print(x,end=' ')
    x -= 1
    print()
print("\n")

'''
    Output
            6
          5 5
        4 4 4
      3 3 3 3
    2 2 2 2 2
  1 1 1 1 1 1
  
    '''


for i in range(6):
    for j in range(i,6):
        print(" ",end=' ')
    for j in range(i+1):
        print(6-1,end=' ')
    print()
print("\n")
'''
    Output
            6
          5 5
        4 4 4
      3 3 3 3
    2 2 2 2 2
  1 1 1 1 1 1

    '''


p = 1
for i in range(6):
    for j in range(i,6):
        print(" ",end=' ')
    for j in range(i+1):
        print(p,end=' ')
        p += 1
    print()

    '''
     Output   
            1
          2 3
        4 5 6
      7 8 9 10
    11 12 13 14 15      
  16 17 18 19 20 21
    '''
