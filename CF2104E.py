import bisect
n,k = map(int, input().split())
s = input()
dp = [0]*n
state = [0]*k

table = [[] for i in range(k)]
for i in range(n-1,-1,-1):
    m = min(state)
    dp[i] = m+1
    state[ord(s[i])-ord('a')]=dp[i]
for i in range(n):
    table[ord(s[i])-ord('a')].append(i)

q =int(input())

for _ in range(q):
    t = input()
    now = -1
    for tt in t:
        arr = table[ord(tt)-ord('a')]
        j = bisect.bisect_left(arr,now)
        if j<len(arr) and arr[j] == now:
            j += 1
        if j < len(arr):
            now = arr[j]
        else:
            print(0)
            break
    else:
        print(dp[now])
    