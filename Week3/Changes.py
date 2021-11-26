n=int(input())
a=0
x=0
while a<=n:
    if a+10<=n:
        a+=10
        x+=1
        continue
    if a+5<=n:
        a+=5
        x+=1
        continue
    if a+1<=n:
        a+=1
        x+=1 
        continue
    else:
        break
print(x)    

