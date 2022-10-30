j=int(input())
k=list(map(int,input().split()))
h, m=map(int,input().split())
l=[]
for i in range(j):
    if k[i]<h or k[i]>m:
        l.append(k[i])
d=len(l)
sum=0
for i in range(d):
   sum+=l[i]
print(sum)