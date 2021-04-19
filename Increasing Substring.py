t=int(input())
def strinc(st):
    temp=0
    for i in range(len(st)):
        if ord(st[i])>temp:
            temp=ord(st[i])
        else:
            break
    else:
        return True
    return False
for t in range(t):
    out=[]
    n=int(input())
    s=str(input())
    i=0
    l=[s[i:j] for j in range(i+1,n+1)]
    for x in l:
        if strinc(x):
            out.append(len(x))
        else:
            j=0-len(x)
            ll=[x[j:] for j in range(len(x)) if strinc(x[j:])]
            ll=[len(x) for x in ll]
            out.append(max(ll))
    print('Case #'+str(t+1)+': '+' '.join([str(x) for x in out]))