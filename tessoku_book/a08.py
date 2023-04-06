# 二次元累積和を計算
def calc_cumulative_sum(H, W, X):
    S = [[0] * (W + 1) for l in range(H + 1)]
    # 行方向の総和を計算
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            S[i][j] = S[i][j - 1] + X[i - 1][j - 1]
    # 列方向の総和を計算
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            S[i][j] += S[i - 1][j]
    return S


# 長方形領域の総和を計算
def calc_area_sum(S, A, B, C, D):
    return S[C][D] + S[A - 1][B - 1] - S[C][B - 1] - S[A - 1][D]


H, W = map(int, input().split())
X = [list(map(int, input().split())) for l in range(H)]
Q = int(input())
A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

S = calc_cumulative_sum(H, W, X)
for i in range(Q):
    print(calc_area_sum(S, A[i], B[i], C[i], D[i]))
