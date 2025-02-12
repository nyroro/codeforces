import heapq
cases = int(input())
for ti in range(cases):
    s = input()
    n,m = [int(t) for t in s.split()]
    s = input()
    a = [-int(t) for t in s.split()]
    s = input()
    b = [-int(t) for t in s.split()]
    sa = sum(a)
    sb = sum(b)
    if sa != sb:
        print("No")
        continue
    heapq.heapify(a)
    heapq.heapify(b)
    while len(b) > 0:
        x = heapq.heappop(b)
        # print(x)
        if x == a[0]:
            heapq.heappop(a)
        elif x > a[0]:
            break
        else:
            x = -x
            t1, t2 = x//2, x-x//2
            heapq.heappush(b, -t1)
            heapq.heappush(b, -t2)
    else:
        print("Yes")
        continue
    print("No")
