import heapq
def solve():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    h = []
    ret = 0
    s = 0
    for i,t in enumerate(arr):
        ret = max(ret, s + i + t + 1)
        heapq.heappush(h, t)
        s += t
        # print(h)
        if len(h)>=k:
            s -= h[0]
            heapq.heappop(h)
    print(ret)
    
solve()