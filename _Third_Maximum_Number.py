n=int(input())
k=list(map(int,input().split()))
k=set(k)
p=sorted(k)
z=[]
for i in p:
    z.append(i)
if n==3:
    print(p[0])
elif n==2:
    print(p[1])
else:
    print(p[-3])
        