for i in range(6):
    for j in range(i+1):
        if j == 0 or i == 6-1 or i == j: 
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
print("\n")

'''
    Output

        * 
        * *
        *   *
        *     *
        *       *
        * * * * * *

'''