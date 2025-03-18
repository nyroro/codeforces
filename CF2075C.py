import bisect
def solve():
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ret = 0
    for i in range(1,n):
        c1 = m-bisect.bisect_left(arr,i)
        c2 = m-bisect.bisect_left(arr,n-i)
        # print(i,c1, c2, arr, c1*c2 - min(c1,c2))
        ret += max(c1*c2 - min(c1,c2), 0)
    print(ret)
for i in range(int(input())):
    solve()