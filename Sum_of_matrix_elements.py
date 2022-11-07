n=int(input())
m=int(input())
b=[]
for i in range(n):
    k=list(map(int,input().split()))
    for j in k:
        b.append(j)
print(sum(b))