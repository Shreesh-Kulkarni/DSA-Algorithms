def maxp(l):
    n=len(l)
    l.sort()
    p=l[-1]*l[-2]
    return p            
if __name__=='__main__':
    n=int(input())
    x=[int(i) for i in input().split()]
    print(maxp(x))



                