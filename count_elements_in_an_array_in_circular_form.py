n=int(input())
l=list(map(int,input().split()))
x=0
for i in range(n-2):
    if l[i]%2==0 and l[i+2]%2!=0:
        x+=1
    elif l[i]%2!=0 and l[i+2]%2==0:
        x+=1
if l[n-2]%2==0 and l[0]%2!=0:
    x+=1
elif l[n-2]%2!=0 and l[0]%2==0:
    x+=1
if l[n-1]%2!=0 and l[1]%2==0:
    x+=1
elif l[n-1]%2==0 and l[1]%2!=0:
    x+=1
print(x)