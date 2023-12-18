#Left angle Traingle pattern 

for i in range(6):
    for j in range(i,6):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print("")

'''
    Output
    
            * 
          * *
        * * *
      * * * *
    * * * * *
  * * * * * *

'''
