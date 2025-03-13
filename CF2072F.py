def gao(x):
    i = 0
    while x%2 == 0:
        i+=1
        x>>=1
    return i
def solve():
    n, k = map(int, input().split())
    n-=1

    c = [0, 0]
    for i in range(2, n+1):
        c.append(c[-1]+gao(i))
    arr = []
    for i in range(n+1):
        arr.append(k if c[n] == c[i]+c[n-i] else 0)
    print(' '.join([str(t) for t in arr]))
for i in range(int(input())):
    solve()
