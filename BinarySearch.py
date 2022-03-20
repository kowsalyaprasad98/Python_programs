p=[int(i) for i in input().split()]
t=int(input())
l=0
h=len(p)
for i in range(l,h):
    mid=(l+h)//2
    if p[mid]==t:
        print("Found")
        break
    elif(p[mid]>t):
        h=mid+1
    elif(p[mid]<t):
        l=mid-1
else:
    print("not found")
