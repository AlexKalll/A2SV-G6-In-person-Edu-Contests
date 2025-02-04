matrix = []
for _ in range(5):
   matrix.append(list(map(int, input().split())))

for i in range(5):
   if 1 in matrix[i]:
        x = i + 1
        y = matrix[i].index(1) + 1
        break
print(abs(3-x) + abs(3-y))

