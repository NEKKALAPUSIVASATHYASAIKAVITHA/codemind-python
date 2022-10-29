
def isprime(n):
    if n==0 or n==1:
        return False
    else:
        sq=int(n**0.5)
        for i in range(2,sq+1):
            if n%i==0:
                return False
        return True
t=int(input())
for i in range(t):
    n=int(input())
    x=0
    y=0
    for i in range(n-1,1,-1):
        if isprime(i):
            x=i
            break
    for i in range(n,100000,1):
        if isprime(i):
            y=i
            break
    if abs(n-x)==abs(n-y):
        print(x)
    elif abs(n-x)>abs(n-y):
        print(y)
    else:
        print(x)