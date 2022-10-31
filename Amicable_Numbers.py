n=int(input())
p=int(input())
s=0
l=0
for i in range(1,n):
    if n%i==0:
        s+=i
for i in range(1,p):
    if p%i==0:
        l+=i
if s==p and l==n:
    print("Amicable")
else:
    print("Not Amicable")
    