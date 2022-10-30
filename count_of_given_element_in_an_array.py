n=int(input())
k=list(map(int,input().split()))
j=int(input())
c=0
for i in range(len(k)):
    if k[i]==j:
        c+=1
if c>=1:
    print(c)
else:
    print("0")