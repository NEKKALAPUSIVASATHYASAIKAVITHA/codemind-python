def isperfect(n):
    p=int(n**0.5)
    if p*p==n:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
z=0
for i in l:
    if isperfect(i):
        z+=i
print(z)