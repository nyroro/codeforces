t = int(input())
for ti in range(t):
    n = int(input())
    s = input()
    arr = [int(t) for t in s.split()]
    even = 0
    odd = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    ans = 0
    now = 0
    while even > 0 or odd > 0:
        if now == 0:
            if even > 0:
                ans += 1
                now = 1
                even -= 1
            else:
                now = 1
                odd -= 1
        else:
            if odd > 0:
                ans += 1
                now = 1
                odd -= 1
            else:
                now = 1
                even -= 1
    print(ans)