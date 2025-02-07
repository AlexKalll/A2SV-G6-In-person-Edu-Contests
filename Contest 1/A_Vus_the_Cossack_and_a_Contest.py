# https://codeforces.com/gym/585107/problem/A

def read_mult():
    return map(int, input().split())


n, m, k = read_mult()
if n <= m and n <= k:
    print('Yes')
else:
    print('No')