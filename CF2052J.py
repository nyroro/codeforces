import bisect
def solve():
    n,m,q = map(int,input().split())
    arr = list(map(int, input().split()))
    d = list(map(int, input().split()))
    l = list(map(int, input().split()))
    s = [l[0]]
    for i in range(1,m):
        s.append(l[i]+s[-1])
    arr = sorted([(d, a) for a, d in zip(arr,d)])
    que = []
    index = 0
    while index < len(arr):
        ed, work_time = arr[index]
        st = ed-work_time
        if len(que) == 0:
            # st, ed, watch_time
            watch_time = st
            que.append((st, ed, watch_time))
            index += 1
        elif st > que[-1][1]:
            watch_time = st - que[-1][1]
            que.append((st, ed, watch_time + que[-1][2]))
            index += 1
        else:
            lst, led, lwatch_time = que[-1]
            que.pop()
            work_time += led-lst
            arr[index] = (ed, work_time)
    # print(que)
    t = list(map(int, input().split()))
    ret = []
    for x in t:
        i = bisect.bisect_left(que, (x, 0x7fffffff, 0))
        if i == 0:
            watch_time = x
        else:
            watch_time = que[i-1][2] + max(x - que[i-1][1], 0)
        j = bisect.bisect_right(s, watch_time)
        ret.append(j)
        # print('For',x)
        # print('Find',i)
        # print('s',s)
        # print('watch_time', watch_time)
        # print('ret', j)
        # print('===============')
    print(' '.join(str(t) for t in ret))
            
    
for i in range(int(input())):
    solve()