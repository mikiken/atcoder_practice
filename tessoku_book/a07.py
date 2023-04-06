D = int(input())
N = int(input())
L = [None] * N
R = [None] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

RF = [0] * (D + 2)
for i in range(N):
    RF[L[i]] += 1
    RF[R[i] + 1] -= 1

S = [0] * (D + 2)
for i in range(1, D + 1):
    S[i] = S[i - 1] + RF[i]

for i in range(1, D + 1):
    print(S[i])
