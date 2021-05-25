t=int(input())
for test in range(1,t+1):
    g=int(input())
    sol=0
    n=1
    x=2*g
    run=True
    while(run):
        k=((x+n)-(n*n))/(2*n)
        if k<=0:
            break
        if k==int(k):
            sol+=1
        n+=1
        
    print("Case #"+str(test)+':',sol)
