N = int(input())
A = list(map(int, input().split()))

# 整数nがk個あるという情報を(n,k)というdictで表す
num_kind = {}
# dicのkeyを作成
for a in A:
    num_kind[a] = 0
# keyに対応する数が何個あるかカウント
for a in A:
    num_kind[a] += 1

# dicを降順にソート(返り値はtupleのlist)
num_kind_list = sorted(num_kind.items(), key=lambda x: x[0], reverse=True)

for num in num_kind_list:
    print(num[1])
# N-n個の0を出力
for i in range(N - len(num_kind_list)):
    print(0)
