def gaomin(x,n,m):
    while x>1 and m > 0:
        if x % 2 == 0:
            m-=1
            x>>=1
        else:
            m-=1
            x>>=1
            x+=1
    while x>0 and n>0:
        n-=1
        x>>=1
    return x

def gaomax(x, n, m):
    while x>0 and n>0:
        n-=1
        x>>=1
    while x > 1 and m > 0:
        if x % 2 == 0:
            m-=1
            x>>=1
        else:
            m-=1
            x>>=1
            x+=1
    return x

def solve():
    x,n,m = map(int, input().split())
    ret_max = gaomax(x,n,m)
    ret_min = gaomin(x,n,m)

    print(ret_min, ret_max)

for i in range(int(input())):
    solve()