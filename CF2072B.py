def solve():
    n = int(input())
    s = input()
    a = s.count('-')
    b = s.count('_')
    v = a//2
    print(b*v*(a-v))
for i in range(int(input())):
    solve()