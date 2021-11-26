def compute_min_refills(distance, tank, stops):
    # write your code here
    if stops[0]>tank:
        return -1
    elif tank>=distance:
        return 0
    else:
        current=0
        num=0
        while current<=len(stops)-2:
            last=current
            while (current<=len(stops)-2 and (stops[current+1]-stops[last]<=tank)):
                current+=1
            if last==current:
                return -1
            if current<=len(stops)-2:
                num+=1
        return num  


if __name__ == '__main__':
    d=int(input())
    m=int(input())  
    s=int(input())
    stops=list(map(int,input().split()))
    stops.insert(0,0)
    stops.append(d)
    print(compute_min_refills(d, m, stops))
