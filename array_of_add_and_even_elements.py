n=int(input())
k=list(map(int,input().split()))
l=[]
c=[]
p=[]
for i in range(n):
    if k[i]%2!=0:
        l.append(k[i])
    elif k[i]%2==0:
        c.append(k[i])
p=l+c
print(*p)