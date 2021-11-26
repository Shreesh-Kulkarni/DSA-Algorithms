# Uses python3
import sys

def get_majority_element(a, left, right):
    f={}
    for i in a:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    for i in f.values():
        if i>len(a)//2:
            return 1
        else:
            return -1                

if __name__ == '__main__':
    n=int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
