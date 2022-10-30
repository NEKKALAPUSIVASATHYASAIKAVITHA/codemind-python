n=int(input())
a=list(map(int,input().split()))
x=[]
p=[]
c=[]
for i in range(n):
    if a[i]%2==0:
        x.append(a[i])
    elif a[i]%2!=0:
        p.append(a[i])
c=x+p
print(*c)