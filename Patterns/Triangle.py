# Square Pattern printing
for i in range(6):
    for j in range(i,6):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')
    print("")

'''
        Output
        
            * 
          * * *
        * * * * *        
      * * * * * * *      
    * * * * * * * * *    
  * * * * * * * * * * *

'''
