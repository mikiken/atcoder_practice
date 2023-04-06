N = int(input())
bin_list = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

for i in range(9, -1, -1):
    bin_list[i] = str(N % 2)
    N = int(N / 2)

binary = "".join(bin_list)
print(binary)
