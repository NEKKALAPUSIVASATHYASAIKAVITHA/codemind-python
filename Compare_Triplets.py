n=list(map(int,input().split()))
m=list(map(int,input().split()))
a=0
b=0
for i in range(len(n)):
    if n[i]>m[i]:
        a+=1
    elif n[i]<m[i]:
        b+=1
print(a,b,end=" ")