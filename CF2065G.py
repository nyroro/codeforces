from collections import Counter
N = 200010
p = [i for i in range(N)]
for i in range(2, N):
    if p[i] == i:
        for j in range(i*i, N, i):
            p[j] = i

t = int(input())
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)
    cnt = Counter()
    pre_p = -1
    pre_cnt = 0
    now_cnt = 0
    ans = 0
    for t in arr:
        if p[t] == t: # is prime
            cnt[t]+=1
            if pre_p == t:
                now_cnt += 1
                ans += pre_cnt
            else:
                pre_cnt += now_cnt
                now_cnt = 1
                pre_p = t
                ans += pre_cnt
        else:
            a = p[t]
            b = t//p[t]
            if p[b] == b:
                if a != b:
                    ans += cnt[a] + cnt[b]
                else:
                    ans += cnt[a]
                cnt[t]+=1
                ans += cnt[t]
        # print('pre', pre_cnt)
        # print('now', now_cnt)
        # print(t, ans)
    print(ans)

for _ in range(t):
    solve()