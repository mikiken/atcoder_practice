from decimal import Decimal, ROUND_HALF_UP

x, k = map(int, input().split())

for i in range(k + 1):
    x = int(Decimal(str(x)).quantize(Decimal("1E" + str(i)), rounding=ROUND_HALF_UP))

print(x)
