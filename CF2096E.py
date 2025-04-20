def solve():
    n = int(input())
    s = input()
    cnt = 0
    ret = 0
    odd = 0
    even = 0
    for i,t in enumerate(s):
        if t == 'B':
            ret += (i-cnt)//2
            if cnt%2 == i%2:
                pass
            elif i%2 == 1:
                odd += 1
            else:
                even += 1
            cnt += 1

    ret += max(odd, even)

    print(ret)


for i in range(int(input())):
    solve()