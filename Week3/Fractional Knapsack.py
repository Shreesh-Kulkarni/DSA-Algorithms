# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    n=len(weights)
    l=[[values[i]/weights[i],i] for i in range(n)]
    l.sort() 
    for i in range(n-1,-1,-1):
        b=l[i][1]
        if weights[b]<=capacity:
            value+=values[b]
            capacity-=weights[b]
        else:
            value+=capacity*l[i][0]    
                

    return value
  


if __name__ == "__main__":
     data = list(map(int, input().split()))
     n, capacity = data[0:2]
     values =[]
     weights =[]
     for i in range(n):
         data1=list(map(int,input().split()))
         value1,weight=data1[0:2]
         values.append(value1)
         weights.append(weight)
     opt_value = get_optimal_value(capacity, weights, values)
     print("{:.10f}".format(opt_value))
