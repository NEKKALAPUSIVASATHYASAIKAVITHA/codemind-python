n=int(input())
x=abs(n)
rev=0
while x:
    d=x%10
    x=x//10
    rev=rev*10+d
if n>=0:
    print(rev)
else:
    print('-',rev,sep="")