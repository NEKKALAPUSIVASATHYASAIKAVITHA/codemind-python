n=int(input())
k=list(map(int,input().split()))
dic={}
for i in k:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
v=list(dic.values())
p=list(dic.keys())
print(p[v.index(max(v))])