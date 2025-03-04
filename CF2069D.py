from collections import Counter
def handle(s):
    n = len(s)
    cc = Counter()
    l = 0
    now = 0
    # print(s)
    while l < n//2 and now < n:
        if n-l-1 < now:
            break
        target = s[n-l-1]
        if l>=now and s[l] == target:
            pass
        elif l<now and cc[target] > 0:
            cc[target] -= 1
        else:
            while now < l:
                now +=1
            while now<n and s[now]!=target:
                cc[s[now]]+=1
                now += 1
            if now<n and s[now] == target:
                now += 1
            # print(l, now, cc)
        l+=1
    return now

def solve():
    s = input()
    n = len(s)
    i=0
    while i<n//2 and s[i]==s[n-i-1]:
        i+=1
    if i==n//2:
        print(0)
        return
    s = s[i:n-i]
    print(min(handle(s), handle(s[::-1])))
for i in range(int(input())):
    solve()