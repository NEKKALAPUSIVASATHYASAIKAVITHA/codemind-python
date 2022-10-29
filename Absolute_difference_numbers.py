n, x=map(int,input().split())
n=str(n)
k=n[:x]
l=n[-x:]
print(abs(int(k)-int(l)))