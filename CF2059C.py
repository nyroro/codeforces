t = int(input())

def solve():
    n = int(input())
    cnt = []
    for i in range(n):
        arr = list(map(int, input().split()))
        c = 0
        for j in range(n-1,-1,-1):
            if arr[j] == 1:
                c += 1
            else:
                break
        cnt.append(c)
    cnt.sort()
    # print(cnt)
    ans = 0
    for t in cnt:
        if t > ans:
            ans += 1
    print(min(ans+1, n))
for _ in range(t):
    solve()