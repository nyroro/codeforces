t = int(input())


def solve():
    arr.sort()
    last_p = 0
    ans = 0
    time = arr[0]
    for i in range(1, n):
        now_p = min(l, arr[i]+time, max(last_p + k, (arr[i]-time + last_p + k)/2))
        time += max(0, now_p - last_p - k)
        ans += min(k, now_p - last_p)
        last_p = now_p
    ans += min(k, l-last_p)
    print(int(2 * (l - ans + arr[0])))

for _ in range(t):
    n,k,l = map(int, input().split())
    arr = list(map(int, input().split()))
    solve()
