# Uses python3
import sys
def mergesort(a,l,r):
    inv=0
    if(l<r):
        m=(l+r)//2
        inv+=mergesort(a,l,m)
        inv+=mergesort(a,m+1,r)
        inv+=merge(a,l,m,r)
    return inv
def merge(a,l,m,r):
    inv=0
    n1=m-l+1
    n2=r-m
    a1,b1=[0*i for i in range(n1)],[0*i for i in range(n2)]
    for i in range(n1):
        a1[i]=a[l+i]
    for i in range(n2):
        b1[i]=a[m+i+1]    
    i=j=0
    k=l
    # Copy data to temp arrays l[] and r[]
    while i < n1 and j < n2:
        if a1[i] <=b1[j]:
            a[k]=a1[i]
            i+=1
            k+=1
        else:
            a[k]=b1[j]
            inv+=n1-i
            j += 1
            k+=1
  
        # Checking if any element was left
    while i <n1:
        a[k]=a1[i]
        i += 1
        k += 1
  
    while j < n2:
        a[k]=b1[j]
        j += 1
        k += 1    
    return inv 

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

if __name__ == '__main__':
    n=int(input())
    a = list(map(int, input().split()))
    print(mergesort(a,0,n-1))
    
