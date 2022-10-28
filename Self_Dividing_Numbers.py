n=int(input())
m=int(input())
for i in range(n,m+1):
    x=i
    e=0
    o=0
    while i:
        d=i%10
        e+=1
        i=i//10
        
        if d!=0:
            if x%d==0:
                o+=1
    if e==o:
        print(x,end=" ")