n=int(input())
k=list(map(int,input().split()))
p=set()
c=0
for i in range(n):
    if k[i]%2==0:
        p.add(k[i])
c=0
for i in p:
    c+=1
print(c)