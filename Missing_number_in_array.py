n=int(input())
s=0
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    p=sum(l)
    z=(k*(k+1))//2
    print(abs(z-p))