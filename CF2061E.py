import heapq
case = int(input())


for ci in range(case):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    p = [[] for i in range(m+1)]

    for i in range(1, 1<<m):
        t = 0x7fffffff

        for j in range(m):
            if (i>>j)&1:
                t&=b[j]
        p[i.bit_count()].append(t)
    s = []
    for i in range(n):
        x = a[i]
        for j in range(1, m+1):
            val = min([(a[i]&q) for q in p[j]])
            s.append(x - val)
            x = val
    s.sort(reverse=True)

    print(sum(a) - sum(s[:k]))