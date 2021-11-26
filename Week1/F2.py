n=int(input())
if n==0:
    print(0)
if n==1:
    print(1)
else:         
    a=n%60
    if a==0:
        print(0)
    else:    
        l=[0*i for i in range(a+1)]
        l[0]=0
        l[1]=1
        for i in range(2,a+1):
            l[i]=l[i-1]+l[i-2]
        print(l[-1]%10)