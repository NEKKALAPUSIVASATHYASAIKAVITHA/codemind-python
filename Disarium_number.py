p=int(input())
n=p
x=str(p)
x=len(x)
i=0
summ=0
while p:
    d=p%10
    p=p//10
    summ+=d**(x-i)
    i+=1
if summ==n:
    print("True")
else:
    print("False")