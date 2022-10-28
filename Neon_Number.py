n=int(input())
x=n*n
s=0
while x:
    d=x%10
    s+=d
    x=x//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    