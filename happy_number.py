n=int(input())
x=n
while True:
    if n==1 or n==7:
        print("True")
        break
    elif n==0 or n==2 or n==3 or n==4 or n==5 or n==6 or n==8 or n==9:
        print("False")
        break
    else:
        x=n
        n=0
        while x:
            d=x%10
            x=x//10
            n+=d**2