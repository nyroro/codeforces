import heapq
def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    st = []
    que = []
    ans = 1
    arr = [0]*n
    cnt0 = 0
    for i in range(n):
        arr[i] = a[i]-b[i]
        if arr[i] == 0:
            cnt0+=1
    if m >= sum(a):
        print(0)
        return
    if cnt0 == n:
        print(1)
        return
    h = []
    for i in range(n):
        t = arr[i]
        if t > 0:
            st.append([t,i])
        elif t<0:
            v = -t
            while len(st)>0 and v > 0:
                x = min(v, st[-1][0])
                dis = 1+i-st[-1][1]
                heapq.heappush(h, [-dis, x])
                v -= x
                st[-1][0]-=x
                if st[-1][0]<=0:
                    st.pop()
            if v > 0:
                que.append([v,i])
    qi = 0
    while len(st)>0:
        t, i = st.pop()
        while t > 0:
            v, j =que[qi]
            dis = 1+j+n-i
            k = min(v,t)
            heapq.heappush(h, [-dis, k])
            que[qi][0]-=k
            t-=k
            if que[qi][0] == 0:
                qi+=1
    while m > 0 and len(h)>0:
        dis,x = h[0]
        t = min(m,x)
        m-=t
        h[0][1]-=t
        if h[0][1] == 0:
            heapq.heappop(h)
    if len(h) == 0:
        print(1)
    else:
        print(-h[0][0])
            

for i in range(int(input())):
    solve()