n = int(input())
s = []
for i in range(n):
    s.append(input())
t = input()
def issub(ss, t):
    if len(ss)<len(t):
        return False
    i = 0
    j = 0
    while i<len(ss) and j<len(t):
        if ss[i] == t[j]:
            i += 1
            j += 1
        else:
            i+=1
    return j == len(t)

for ss in s:
    if issub(ss,t):
        print('NO')
        exit(0)

index_t = 0
ind = [0] * n
cha = [[] for i in range(26)]
que = []
ans = []
sat = 0
qi = 0
for i, ss in enumerate(s):
    c = ord(ss[0]) - ord('a')
    if len(cha[c]) == 0 and ss[0] != t[0]:
        que.append(c)
    cha[c].append(i)
# print('que',que)
while sat < n:
    # print('sat', sat, n, ind)
    if qi >= len(que):
        c = ord(t[index_t]) - ord('a')
        ans.append(t[index_t])
        index_t += 1
        # print('add index_t', index_t)
        arr = cha[c]
        cha[c] = []
        for i in arr:
            ind[i]+=1
            if ind[i] == len(s[i]):
                sat += 1
            else:
                si = s[i][ind[i]]
                cc = ord(si) - ord('a')
                if len(cha[cc]) == 0 and si != t[index_t]:
                    que.append(cc)
                cha[cc].append(i)
    else:
        c = que[qi]
        # print('handle', c, ans)
        qi += 1
        ans.append(chr(ord('a')+c))
        arr = cha[c]
        cha[c] = []
        for i in arr:
            ind[i]+=1
            if ind[i] == len(s[i]):
                sat += 1
            else:
                si = s[i][ind[i]]
                cc = ord(si) - ord('a')
                if len(cha[cc]) == 0 and si != t[index_t]:
                    que.append(cc)
                cha[cc].append(i)
print('YES')
print(''.join(ans))
