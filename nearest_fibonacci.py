n=int(input())
a=0
b=1
x=0
y=0
while n:
    c=a+b
    a=b
    b=c
    if c<n:
        x=c
    elif c>=n:
        y=c
        break
if abs(n-x)==abs(n-y):
    print(x,y,end=" ")
elif abs(n-x)>abs(n-y):
    print(y)
else:
    print(x)
        