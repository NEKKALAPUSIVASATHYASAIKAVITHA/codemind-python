def isprime(n):
    if n==0 or n==1:
        return False
    s=int(n**0.5)
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
if isprime(n):
    print("prime")
else:
    print("not a prime")