from random import getrandbits
f=getrandbits(20)
def solve():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    table = {}
    index = {}
    for i,t in enumerate(a):
        table.setdefault(t^f, []).append(i)
        index[t^f] = 0
    qarr = []
    for i in range(q):
        k,l,r = map(int,input().split())
        qarr.append((l,r,k,i))
    qarr.sort()
    ans = [0]*q
    now = 0
    # print(table)
    # print(index)
    for l,r,k,ai in qarr:
        l-=1
        r-=1
        # print(l,r,k,ai)
        while now < l:
            index[a[now]^f]+=1
            now += 1
        fact = []
        i = 1
        while i*i<=k:
            if k%i == 0:
                if i^f in table and index[i^f] < len(table[i^f]):
                    ti = table[i^f][index[i^f]]
                    if ti<=r:
                        fact.append(ti)
                j = k//i
                if j != i and j^f in table and index[j^f] < len(table[j^f]):
                    ti = table[j^f][index[j^f]]
                    if ti<=r:
                        fact.append(ti)
            i+=1
        # print(f)
        fact.sort()
        x = l
        ret = 0
        for ti in fact:
            rr = ti - x
            val = a[ti]
            
            ret += k*rr
            while k%val == 0:
                k//=val
            # print('cal', ti,k,ret)
            x = ti
        if len(fact) == 0:
            ret = k * (r-l+1)
        else:
            ret += (r-x+1)*k
        ans[ai] = ret

    for t in ans:
        print(t)


for i in range(int(input())):
    solve()