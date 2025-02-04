t = int(input())
for _ in range(t):
    n = int(input())
    zeros = str(n).count('0')
    k = len(str(n)) - zeros

    print(k)
    strn = str(n)
    length = len(strn)
    ans = []
    for i in range(length):
        if strn[i] != '0':
            curr = strn[i] + '0' * ( length - i - 1)
            ans.append(int(curr))

    print(*ans)