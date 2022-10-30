
n=int(input())
k=list(map(int,input().split()))
s=0
c=0
average=0
for i in range(n):
    s+=k[i]
average=s//n
for i in range(n):
    if k[i]>=average:
        c+=1
print(c)