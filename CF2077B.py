import sys
n1 = 0
n2 = 0
for i in range(15):
    n1<<=2
    n1 += 1
    n2<<=2
    n2 += 2
# print(bin(n1))
# print(bin(n2))
def solve():
    print(n1)
    sys.stdout.flush()
    t1 = int(input())
    print(n2)
    sys.stdout.flush()
    t2 = int(input())
    x = 0
    y = 0
    for i in range(15):
        if t2 & 1:
            y += 1<<(2*i)
        elif t2 & 2:
            x += 1<<(2*i)
            y += 1<<(2*i)
        t2 >>= 2
        t2 -= 1
        if (t1 & 2) == 0:
            y += 1<<(2*i+1)
            t1 -= 4
        elif t1&4:
            x += 1<<(2*i+1)
            y += 1<<(2*i+1)
            t1 -= 4
        t1 >>= 2
    # print('x,y', x,y)
    print('!')
    sys.stdout.flush()
    m = int(input())
    print((x|m)+(y|m))
for i in range(int(input())):
    solve()