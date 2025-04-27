N=29

def solve():
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if k == 0:
        print(1)
        return
    tries = [-1, -1, -1]

    m = 1

    ret = n+1
    for j,t in enumerate(arr):
        v = t^k
        now_index = 0
        ans = -1
        
        for i in range(N,-1,-1):
            if ((k>>i) & 1) == 0:
                tt = ((t>>i)&1)^1
                tmp_index = tries[3*now_index + tt]
                if tmp_index >=0:
                    ans = max(ans, tries[3*tmp_index + 2])
            tt = (v>>i)&1
            next_index = tries[3*now_index+tt]
            if next_index < 0:
                break
            else:
                now_index = next_index
        else:
            ans = max(ans, tries[3*now_index+2])

        if ans >= 0:
            ret = min(ret, j-ans+1)
        
        now_index = 0

        for i in range(N,-1,-1):
            val = (t>>i) & 1
            next_index = tries[3*now_index+val]
            if next_index < 0:
                new_node = [-1,-1, j]
                new_index = m
                m+=1
                tries.extend(new_node)
                tries[3*now_index+val] = new_index
                now_index = new_index
            else:
                now_index = next_index
                tries[3*now_index+2] = j
    if ret > n:
        ret = -1
    print(ret)
for case in range(int(input())):
    solve()