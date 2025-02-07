
t = int(input())
for _ in range(t):
    s = input()

    n = len(s)
    if n % 2 != 0:
        print('NO')
    else:
        if s[:n//2] == s[n//2:]:
            print('YES')
        else:
            print('NO')
