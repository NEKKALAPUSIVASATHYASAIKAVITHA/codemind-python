def uglynum(n):
    if n==0:
        return False
    for i in [2,3,5]:
        while n%i==0:
            n=n/i
    return n==1
n=int(input())
if uglynum(n):
    print("Ugly Number")
else:
    print("Not Ugly Number")