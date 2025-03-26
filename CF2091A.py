from collections import Counter
def solve():
    n = int(input())
    c = Counter([2,0,2,5,0,1,0,3])
    arr = list(map(int, input().split()))
    for i, t in enumerate(arr):
        c[t] = max(c[t]-1, 0)
        if sum(c.values()) == 0:
            print(i+1)
            return
    print(0)
for i in range(int(input())):
    solve()