#Left angle triangle mirror pattern

for i in range(6):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,6):
        print("*",end=' ')
    print("")

'''
    Output
    
    * * * * * * 
      * * * * *
        * * * *
          * * *
            * *
              *  

'''
