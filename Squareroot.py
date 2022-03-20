x=int(input())
l=0
u=x
c=1
if x==0 or x==1:
    print(x)
while(l<=u):
    p=(l+u)//2
    sq=p*p
    if sq==x:
        print(p)
    elif sq>x:
        u=p-1
    elif sq<x:
        l=p+1
        c=p
print(c)
