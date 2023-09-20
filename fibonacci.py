#Fibonacchi Number

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
num = int(input("Enter the fib number: "))
print("The fiboncci of ",num,"is" ,fib(num))


print("\n")
def table(n,i):
    if i>10:
        return
    print(n,"*",i,"=",n*i)
    return table(n,i+1)

n=int(input("num: "))
i=int(input("iteration: "))
table(n,i)
