# Outer Square pattern printing

for i in range(6):
    for j in range(6):
        if (i == 0 or i == 6-1) or (j == 0 or j == 6-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print("\n")

'''
    Output

    * * * * * * 
    *         * 
    *         *
    *         *
    *         *
    * * * * * *
    
'''

# Cross (X) pattern printing

for i in range(7):
    for j in range(7):
        if (i == j) or (i + j == 7-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print("\n")

'''
    Output

    *           *
      *       *
        *   *
          *
        *   *
      *       *
    *           *

'''


# Outer Square and X pattern printing

for i in range(7):
    for j in range(7):
        if (i == j) or (i + j == 7-1) or (i == 0 or i == 7-1) or (j == 0 or j == 7-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print("\n")

'''
    Output

    * * * * * * *
    * *       * *
    *   *   *   *
    *     *     *
    *   *   *   *
    * *       * *
    * * * * * * *

'''

# + pattern printing

for i in range(7):
    for j in range(7):
        if (i == 6 // 2) or (j == 6 // 2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

'''
        Output

              *
              *
              *
        * * * * * * *
              *
              *
              *
'''
