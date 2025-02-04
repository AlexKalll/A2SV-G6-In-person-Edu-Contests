
n, k = map(int, input().split())

a = list(map(int, input().split()))

count = 0

for num in a:
    if num >= a[k-1] and num > 0:
        count += 1

print(count)