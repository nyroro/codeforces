def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    zero = 0
    seg = 0
    flag = False
    for t in arr:
        if t != 0 and not flag:
            flag = True
            seg += 1
        elif t==0:
            flag = False
    
    print(min(seg, 2))
for i in range(int(input())):
    solve()