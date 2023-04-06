# 時刻tにおける全プリンターの出力枚数の合計
def calc_flyer_sum(t, N, A):
    sum = 0
    for i in range(N):
        sum += t // A[i]
    return sum


# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索の初期値
T_left = 1
T_right = 10**9

while T_left < T_right:
    T_mid = (T_left + T_right) // 2
    if calc_flyer_sum(T_mid, N, A) < K:
        T_left = T_mid + 1
    else:
        T_right = T_mid

print(T_left)
