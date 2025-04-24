
# fibonacci series

def fibo(n):

    if(n == 0 or n == 1):
        return n    
    
    return fibo(n-2) + fibo(n-1)

n = int(input("enter number to find fibonacci : "))
res = fibo(n)
print(res)