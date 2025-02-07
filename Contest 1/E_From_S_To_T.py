"""# https://codeforces.com/gym/585107/problem/E

from collections import Counter
q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()

    p_cnt = Counter(p)

    if len(s) > len(t):
        print('NO')
        continue
    
    s = list(s)
    for i in range(len(t)):
        if i >= len(s):
            if t[i] in p_cnt and p_cnt[t[i]] > 0:
                p_cnt[t[i]] -= 1
                s.append(t[i])
            else:
                break

        elif s[i] != t[i]:
            if t[i] in p_cnt and p_cnt[t[i]] > 0:
                p_cnt[t[i]] -= 1
                s.insert(i, t[i])
            else:         
                break

    s == ''.join(s)
    if len(s) != len(t):
        print('NO')
        continue

    for i in range(len(t)):
        if s[i] != t[i]:
            print('NO')
            break
    else:
        print('YES')
"""
from collections import Counter
q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()

    p_cnt = Counter(p)

    sp, tp = 0, 0 # pointer for s and t
    while tp < len(t):
        if sp < len(s) and t[tp] == s[sp]:
            sp += 1
        else:
            if t[tp] in p_cnt:
                p_cnt[t[tp]] -= 1
                if p_cnt[t[tp]] == 0:
                    del p_cnt[t[tp]]
            else:
                print('NO')
                break   
        tp += 1 
        
    else:   
        # check if there is any character left in s unmatched
        if sp == len(s):
            print('YES')
        else:
            print('NO')