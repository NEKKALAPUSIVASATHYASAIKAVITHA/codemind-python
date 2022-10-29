n=int(input())
k=list(map(int,input().split()))
s=0
for i in range(0,len(k)):
    if i%2!=0:
        s+=k[i]
print(s)