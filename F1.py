n=int(input())
l=[0*i for i in range(n+1)]
if n==0:
    print(0)
elif n==1:
    print(1)
else:        
    l[0]=0
    l[1]=1
    for i in range(2,n+1):
        l[i]=l[i-1]+l[i-2]
    print(l[-1])             