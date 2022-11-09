t=int(input())
while(t):
    r=0
    m=0
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(0,n-1):
        if(arr[i]>arr[i+1]):
            r+=1
    if(r!=0):
        for i in range(0,n):
            for j in range(0,n-1):
                if(arr[j]>arr[j+1]):
                    p=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=p
        m=arr[n-1]-arr[0];
        print(m)
    else:
        print("0")
        t-=1