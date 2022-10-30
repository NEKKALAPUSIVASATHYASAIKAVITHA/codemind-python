n=int(input())
k=list(map(int,input().split()))
o=0
z=0

for i in range(n):
    if k[i]==1:
        o+=1
    elif k[i]==0:
        z+=1
p=o+z
if p==n:
    print("True")
else:
    print("False")

        