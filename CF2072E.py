def solve():
    k = int(input())
    if k==0:
        print(0)
        return
    arr = [(0,0)]
    val = 0
    n = 1
    while val + n <= k:
        arr.append((n,0))
        val += n
        n+=1
    i = 0
    temp = 1
    while val < k:
        n = 1
        while val + n <= k:
            arr.append((i, temp))
            val += n
            n += 1
            temp += 1
        i += 1
    print(len(arr))
    for t in arr:
        print(t[0], t[1])
for i in range(int(input())):
    solve()