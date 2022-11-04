n=int(input())
p=0
s=0
for i in range(n):
    k=list(map(int,input().split()))
    p+=k[i]
    s+=k[n-(i+1)]
print("Principal Diagonal:",p,sep="")
print("Secondary Diagonal:",s,sep="")