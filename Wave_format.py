n=int(input())
k=list(map(int,input().split()))
l=sorted(k)
z=[]
while len(z)<n:
    if len(l)>=2:
        z.append(l[-2])
        z.append(l[-1])
        del l[-1]
        del l[-1]
    else:
        z.append(l[-1])
print(*z)
        