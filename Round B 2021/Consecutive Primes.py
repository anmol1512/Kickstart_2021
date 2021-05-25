import sympy as s
t=int(input())
for k in range(t):
    z=int(input())
    temp=1
    p1=2
    p2=3
    run=True
    while run:
        if p1*p2<=z:
            p1=s.nextprime(p1)
            p2=s.nextprime(p2)
            temp=s.nextprime(temp)
        else:
            run=False
    print('Case #'+str(k+1)+': '+str(temp*p1))