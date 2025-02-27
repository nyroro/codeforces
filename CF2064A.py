t = int(input())
def solve():
    n = input()
    s = input()
    now = s[0]
    cnt = 0
    if now == '1':
        cnt = 1
    for t in s:
        if t != now:
            cnt += 1
            now = t
    print(cnt)
for _ in range(t):
    solve()