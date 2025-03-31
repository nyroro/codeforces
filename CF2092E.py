mod = int(1e9)+7
def solve():
    n,m,k = map(int, input().split())
    cnt1 = (n-2)*(m-2)+4
    cnt2 = 2*(n-2)+2*(m-2)
    black = 0
    for i in range(k):
        x,y,c = map(int,input().split())
        if x == 1 or x == n:
            if y != 1 and y != m:
                cnt2 -= 1
                if c == 1:
                    black += 1
            else:
                cnt1 -= 1
        elif y == 1 or y == m:
            if x != 1 and x != n:
                cnt2 -= 1
                if c == 1:
                    black += 1
            else:
                cnt1 -= 1
        else:
            cnt1 -= 1
    if cnt2 == 0 and black % 2 == 1:
        print(0)
        return
    ret = pow(2, cnt1, mod)
    if cnt2 > 0:
        ret = ret * pow(2, cnt2-1, mod)%mod
    print(ret)
for i in range(int(input())):
    solve()