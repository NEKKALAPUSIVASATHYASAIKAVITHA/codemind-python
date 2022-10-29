n=int(input())
sq=int(n**0.5)
f=0
for i in range(2,sq+1):
    if n%i==0:
        if i*(i+1)==n:
            f=1
if f!=0:
    print("YES")
else:
    print("NO")