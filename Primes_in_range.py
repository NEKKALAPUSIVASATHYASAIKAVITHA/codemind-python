def isprime(n):
    if n==0 or n==1:
        return False
    else:
        sq=int(n**0.5)
        for i in range(2,sq+1):
            if n%i==0:
                return False

        return True
c=0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if isprime(i):
        c+=1
print(c)