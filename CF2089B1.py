from collections import deque
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
    if cnt0 == n:
        print(1)
        return
    for i in range(n):
        t = arr[i]
        if t > 0:
            st.append([t,i])
        elif t<0:
            v = -t
            while len(st)>0 and v > 0:
                x = min(v, st[-1][0])
                ans = max(ans, 1+i-st[-1][1])
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
            ans = max(ans, 1+j+n-i)
            k = min(v,t)
            que[qi][0]-=k
            t-=k
            if que[qi][0] == 0:
                qi+=1
    print(ans)

            

for i in range(int(input())):
    solve()