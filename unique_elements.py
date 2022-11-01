n=int(input())
l=list(map(int,input().split()))
z=[]
for i in range(n):
    c=0
    for j in range(i+1):
        if l[i]==l[j]:
            c+=1
    if c==1:
        z.append(l[i])
print(*z)