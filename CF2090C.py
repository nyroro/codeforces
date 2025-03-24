import heapq
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    h_all = [(2, 1, 1)]
    h_table = [(2, 1, 1)]
    vis = set([(1,1)])
    occ = set()
    ans = []
    for t in arr:
        if t == 0:
            _, x, y = heapq.heappop(h_table)
            while (x,y) in occ:
                _,x,y = heapq.heappop(h_table)
            occ.add((x,y))
            print(x,y)
        else:
            _, x, y = heapq.heappop(h_all)
            while (x,y) in occ:
                _,x,y = heapq.heappop(h_all)
            occ.add((x,y))
            print(x,y)
        if x%3 == 1 and y%3 == 1:
            v1 = (x+1+y,x+1,y)
            v2 = (x+y+1,x,y+1)
            v3 = (x+2+y+2,x+1, y+1)
            v4 = (x+3+y,x+3,y)
            v5 = (x+3+y,x,y+3)
            if v1 not in vis:
                heapq.heappush(h_all, v1)
                vis.add(v1)
            if v2 not in vis:
                heapq.heappush(h_all, v2)
                vis.add(v2)
            if v3 not in vis:
                heapq.heappush(h_all, v3)
                vis.add(v2)
            if v4 not in vis:
                heapq.heappush(h_table, v4)
                heapq.heappush(h_all,v4)
                vis.add(v4)
            if v5 not in vis:
                heapq.heappush(h_table, v5)
                heapq.heappush(h_all,v5)
                vis.add(v5)

                    
for i in range(int(input())):
    solve()