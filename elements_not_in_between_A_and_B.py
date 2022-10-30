n=int(input())
k=list(map(int,input().split()))
m, o=map(int,input().split())
l=[]
for i in range(n):
    if k[i]<m or k[i]>o:
        l.append(k[i])
if l==[]:
    print("-1")
else:
    print(*l)