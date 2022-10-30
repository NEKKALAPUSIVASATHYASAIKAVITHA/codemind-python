n=int(input())
k=list(map(int,input().split()))
x=0
if n==0:
    print("0")
else:
    for i in range(n-2):
        if k[i]%2==0 and k[i+2]%2!=0:
            x+=1
        elif k[i]%2!=0 and k[i+2]%2==0:
            x+=1
print(x)