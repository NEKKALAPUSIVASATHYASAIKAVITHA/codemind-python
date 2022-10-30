n=int(input())
k=list(map(int,input().split()))
p=int(sum(k)/len(k))+1
c=0
for i in range(n):
    if k[i]<p:
        c+=1
print(c)