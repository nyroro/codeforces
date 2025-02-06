t = input()
for ti in range(int(t)):
    l, r = map(int, input().split())
    if l == r:
        print(0 if l != 1 else 1)
    else:
        print(r-l)