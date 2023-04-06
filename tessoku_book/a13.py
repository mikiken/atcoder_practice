N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0] * (N - 1)

# lは 0 から N-2 を動く
for l in range(0, N - 1):
    # R[l] の初期値を決定
    if l == 0:
        R[l] = 0
    else:
        R[l] = R[l - 1]
    # 差がK以下となるような最大のRの場所を探す
    # Rが1番右に来た時点で、残りのlについてもRの位置は1番右となる
    while R[l] < N - 1 and A[R[l] + 1] - A[l] <= K:
        R[l] += 1

count = 0
for l in range(0, N - 1):
    count += R[l] - l

print(count)
