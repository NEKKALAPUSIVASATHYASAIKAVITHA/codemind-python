n=int(input())
k=list(map(int,input().split()))
p, q=map(int,input().split())
l=[]
c=0
for i in range(n):
    if k[i]<p or k[i]>q:
        l.append(k[i])
if l==[]:
    print("-1")
else:
    print(max(l))