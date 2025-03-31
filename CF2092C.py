def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    t1 = [t for t in arr if t % 2==1]
    t2 = [t for t in arr if t%2 ==0]
    if len(t1) == 0 or len(t2) == 0:
        print(max(arr))
        return
    else:
        print(sum(arr) - (len(t1)-1))
for i in range(int(input())):
    solve()