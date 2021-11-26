# Uses python3
inf =float('inf')
def min(x,y):
    if x<y:
        return x
    else:
        return y    

def get_change(m):
    #write your code here
    d=[0,1,3,4]
    a=[0]*(m+1)
    for i in range(1,m+1):
        minimum=inf
        for j in range(1,4):
            if (i>=d[j]):
                minimum=min(minimum,1+a[i-d[j]])
        a[i]=minimum
    return a[m]    
        
   

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
