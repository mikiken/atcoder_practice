def calc_max_left(N, A):
    P = [0] * (N + 2)
    for i in range(1, N + 1):
        P[i] = max(P[i - 1], A[i - 1])
    return P


def calc_max_right(N, A):
    Q = [0] * (N + 2)
    for i in range(N, 0, -1):
        Q[i] = max(A[i - 1], Q[i + 1])
    return Q


# 入力
N = int(input())
A = list(map(int, input().split()))
D = int(input())
L = [None] * D
R = [None] * D
for d in range(D):
    L[d], R[d] = map(int, input().split())

# 左右から"累積最大値"を計算
P = calc_max_left(N, A)
Q = calc_max_right(N, A)

# 出力
for d in range(D):
    P_max = P[L[d] - 1]
    Q_max = Q[R[d] + 1]
    print(max(P_max, Q_max))
