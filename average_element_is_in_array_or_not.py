n=int(input())
k=list(map(int,input().split()))
p=int(sum(k)/len(k))
f=0
for i in range(len(k)):
    if k[i]==p:
        f=1
if f==1:
    print("True")
else:
    print("False")