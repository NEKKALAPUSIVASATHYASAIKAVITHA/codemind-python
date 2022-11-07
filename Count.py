n=int(input())
l=list(map(int,input().split()))
oc=0
ec=0
for i in l:
    if i%2==0:
        ec+=1
    else:
        oc+=1
print(ec,oc,end=" ")