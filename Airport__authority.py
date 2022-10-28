n=int(input())
l=[]
for i in range(n):
    k=int(input())
    l.append(k)
t=int(input())
s=0
for x in l:
    if x>t:
        s+=2
    else:
        s+=1
print(s)