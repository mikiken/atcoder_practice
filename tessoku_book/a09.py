# 二次元累積和を計算
def calc_cumulative_sum(H, W, RF):
    S = [[0] * (W + 1) for l in range(H + 1)]
    # 行方向の累積和を計算
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            S[i][j] = S[i][j - 1] + RF[i][j]
    # 列方向の累積和を計算
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            S[i][j] += S[i - 1][j]
    return S


# 入力
H, W, N = map(int, input().split())
A = [None] * N
B = [None] * N
C = [None] * N
D = [None] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 差分を記録
RF = [[0] * (W + 2) for l in range(H + 2)]
for i in range(N):
    RF[A[i]][B[i]] += 1
    RF[C[i] + 1][D[i] + 1] += 1
    RF[A[i]][D[i] + 1] -= 1
    RF[C[i] + 1][B[i]] -= 1

# 出力
Z = calc_cumulative_sum(H, W, RF)
for i in range(1, H + 1):
    for j in range(1, W + 1):
        print(Z[i][j], end=" ")
    print("")
