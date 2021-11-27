# Uses python3
import sys

def optimal_weight(W, w):
    w=[0]+w
    weights=[[0 for _ in range(len(w))] for _ in range(W+1)]
    for i in range(1,len(w)):
        for j in range(1,W+1):
            weights[j][i] = weights[j][i - 1]
            if w[i] <= j:
                val = weights[j - w[i]][i - 1] + w[i]
                if weights[j][i] < val:
                    weights[j][i] = val
    return weights[-1][-1]                

if __name__ == '__main__':
    n=list(map(int,input().split()))
    W=n[0]
    w=list(map(int,input().split()))
    print(optimal_weight(W, w))
