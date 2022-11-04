n=int(input())
a=list(map(int,input().split()))
l=[]
m=n//2
for i in range(m):
    l.append(a[-i-1])
for j in range(m):
    l.append(a[j])
print(*l)
