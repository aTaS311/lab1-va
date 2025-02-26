import math
m = (2.56 * 0.75) * math.sin(2) + (5.5 * 0.33) * math.sin(3)
n = (math.pi / 6) * math.log(2) + math.sin(math.cos(7) - math.cos(13 / 14))
if abs(m) + abs(n) > 1:
    k = (m - n) / (3 * m*2 - 4 * n*2)
else:
    k = m*2 * n*2
print(f"m = {m}")
print(f"n = {n}")
print(f"k = {k}")
