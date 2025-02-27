t = int(input())
def handle(x, s, k):
    for t in s:
        x += t
        k -= 1
        if x == 0:
            break
        if k == 0:
            break
    return x, k
def solve():
    n,x,k = map(int, input().split())
    s = input()
    if x < 0:
        s = [-1 if t =='R' else 1 for t in s]
        x = -x
    else:
        s = [-1 if t == 'L' else 1 for t in s]

    x, k = handle(x,s,k)
    if x != 0:
        print(0)
        return
    cnt = 0
    if x == 0 and k>=0:
        cnt += 1
        # print('first',cnt,k)
        if k > 0:
            # print('second', k)
            x, nk = handle(x, s, k)
            step = k-nk
            if x == 0:
                cnt += k//step

    print(cnt)
    
for _ in range(t):
    solve()