n=input()
k=list(map(int,input().split()))
l=int(input())
f=0
for i in range(len(k)):
    if k[i]==l:
        f=1
if f==1:
    print("True")
else:
    print("False")