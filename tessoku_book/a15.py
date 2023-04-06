import bisect

N = int(input())
A = list(map(int, input().split()))

# Aを昇順にソートし、重複を削除したリストを作成
A_modified = sorted(list(set(A)))

# Aの各数字がA_modifiedの何番目にあるかをBに記録
B = []
for i in range(N):
    l = bisect.bisect_left(A_modified, A[i])
    if l < N and A_modified[l] == A[i]:
        # A_modifiedでの位置は0スタートなので1加える
        B.append(l + 1)

for i in range(N):
    print(B[i], end=" ")
