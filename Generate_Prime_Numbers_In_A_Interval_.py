def isprime(n):
    if n==0 or n==1:
        return False
    else:
        s=int(n**0.5)
        for i in range(2,s+1):
            if n%i==0:
                return False
        return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if isprime(i):
        
        print(i)