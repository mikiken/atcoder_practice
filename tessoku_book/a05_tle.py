N, K = map(int, input().split())

count = 0
for r in range(1, N + 1):
    for b in range(1, N + 1):
        w = K - r - b
        if 1 <= w and w <= N:
            count += 1

print(count)
