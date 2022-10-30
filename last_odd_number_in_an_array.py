n=int(input())
k=list(map(int,input().split()))
x=0
for i in range(n):
    if k[i]%2!=0:
        x=k[i]
print(x)