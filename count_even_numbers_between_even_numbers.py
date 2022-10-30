n=int(input())
k=list(map(int,input().split()))
x=0
for i in range(n-2):
    if k[i]%2==0 and k[i+1]%2==0 and k[i+2]%2==0:
        x+=1
print(x)