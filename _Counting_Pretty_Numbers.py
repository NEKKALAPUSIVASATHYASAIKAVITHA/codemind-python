def ispretty(n):
    rem=n%10
    if rem == 2 or rem==3 or rem==9:
         return True
    return False
l=int(input())
for i in range(l):
    m,n=map(int,input().split())
    c=0
    for i in range(m,n+1):
        if(ispretty(i)):
            c+=1
    print(c)