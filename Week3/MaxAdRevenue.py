def maxrevenue(p,c,n):
    p.sort()
    c.sort()
    max=0
    for i in range(n):
        max+=p[-1]*c[-1]
        p.pop()
        c.pop()
    return max
    
if __name__=='__main__':
    n=int(input())
    p=list(map(int,input().split()))
    c=list(map(int,input().split()))
    print(maxrevenue(p,c,n))

