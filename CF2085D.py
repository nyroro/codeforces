import heapq
N = 200010
vis = [False]*N
def solve():
    n,k = map(int,input().split())
    arr = map(int, input().split())
    pn = n//(k+1)
    h = []
    ret = 0
    for i,t in enumerate(arr):
        heapq.heappush(h, -t)
        if n-i == pn*(k+1):
            ret += -h[0]
            heapq.heappop(h)
            pn -= 1

    print(ret)

for i in range(int(input())):
    solve()