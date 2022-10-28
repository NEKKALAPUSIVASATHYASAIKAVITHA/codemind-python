def fibofun(n):
    if n==0 or n==1:
        return n
    else:
        return fibofun(n-1)+fibofun(n-2)
n=int(input())
for i in range(n):
    print(fibofun(i),end=" ")