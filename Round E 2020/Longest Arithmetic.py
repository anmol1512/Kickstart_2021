t=int(input())
for k in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    i=0
    j=1
    d=a[i]-a[j]
    count=2
    temp=0
    run=True
    while run:
        i+=1
        j+=1
        if j<=n-1:
            if a[i]-a[j]==d:
                count+=1
            else:
                d=a[i]-a[j]
                if count>temp:
                    temp=count
                count=2
        else:
            run=False
    if count>temp:
        temp=count
    if temp==0:
        print('Case #'+str(k+1)+': '+str(count))
    else:
        print('Case #'+str(k+1)+': '+str(temp))