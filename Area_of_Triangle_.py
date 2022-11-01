import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
l=((s-a)*(s-b)*(s-c)*s)
p=math.sqrt(l)
print("%.2f"%p)