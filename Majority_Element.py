n=int(input())
k=list(map(int,input().split()))
p=n/2
dic={}
for i in k:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for key,values in dic.items():
    if values>p:
        print(key)