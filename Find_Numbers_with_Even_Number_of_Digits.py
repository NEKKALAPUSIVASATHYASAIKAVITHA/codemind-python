def iseven(n):
    c=0
    while n:
        d=n%10
        n=n//10
        c+=1
    if c%2==0:
        return True
    else:
        return False
n=int(input())
k=list(map(int,input().split()))
p=0
for i in k:
    if iseven(i):
        p+=1
print(p)