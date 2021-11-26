# Uses python3
def edit_distance(s, t,m,n):
    d=[[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                d[i][j]=j
            elif j==0:
                d[i][j]=i
            elif s[i-1]==t[j-1]:
                d[i][j]=d[i-1][j-1]
            else:
                d[i][j]=1+min(d[i-1][j],d[i][j-1],d[i-1][j-1]) 
    return d[m][n]            




if __name__ == "__main__":
    s=input()
    t=input()
    print(edit_distance(s,t,len(s),len(t)))
