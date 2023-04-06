N, X = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = N

while L <= R:
    M = (L + R) // 2
    if X == A[M]:
        print(M + 1)
        exit()
    elif X <= A[M]:
        R = M - 1
    else:
        L = M + 1
