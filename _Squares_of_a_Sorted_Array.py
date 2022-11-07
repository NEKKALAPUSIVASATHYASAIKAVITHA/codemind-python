n=int(input())
l=list(map(int,input().split()))
z=[]
for i in l:
    p=i*i
    z.append(p)
z=sorted(z)
print(*z)
    