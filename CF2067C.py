def solve():
    n = int(input())
    for i in range(10):
        s = str(n-i)
        md = 0
        for c in s:
            vc = int(c)
            if vc<=7:
                md = max(md, vc)
        if i >= 7-md:
            print(i)
            return

for _ in range(int(input())):
    solve()