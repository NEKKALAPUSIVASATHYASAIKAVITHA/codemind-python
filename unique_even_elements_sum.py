n=int(input())
k=list(map(int,input().split()))
p=set()
for i in range(n):
    if k[i]%2==0:
        p.add(k[i])
s=0
for i in p:
    s+=i
print(s)
    