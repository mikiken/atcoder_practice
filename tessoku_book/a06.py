import itertools

N, Q = map(int, input().split())
A = list(map(int, input().split()))
days = [list(map(int, input().split())) for l in range(Q)]

S = list(itertools.accumulate(A))
S.insert(0, 0)

for d in days:
    print(S[d[1]] - S[d[0] - 1])
