k=int(input())
l=list(map(int,input().split()))
n=int(input())
for i in range(n):
    l.insert(0,l[-1])
    l.pop(-1)
print(*l)