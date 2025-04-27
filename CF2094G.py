from collections import deque
def solve():
    q = int(input())
    d = deque()
    r = False
    ansl = 0
    ansr = 0
    s = 0
    for i in range(q):
        ss = input()
        if ss.startswith('3'):
            _, k = map(int, ss.split())
            if r:
                d.appendleft(k)
                ansl = k +ansl + s
                ansr = k*len(d)+ansr
                s += k
                print(ansr)
            else:
                d.append(k)
                ansl = k*len(d)+ansl
                ansr = k + ansr+s
                s+=k
                print(ansl)
        elif ss == '2':
            r = not r
            print(ansr if r else ansl)
        else:
            if r:
                v = d.popleft()
                ansl -= s
                ansr -= v*(len(d)+1)
                d.append(v)
                ansl += v*len(d)
                ansr += s
                print(ansr)
            else:
                v = d.pop()
                ansl -= v*(len(d)+1)
                ansr -= s
                d.appendleft(v)
                ansl += s
                ansr += v*len(d)
                print(ansl)

        
for i in range(int(input())):
    solve()