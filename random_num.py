from blueqat import Circuit as C

from time import time

# 0~2^n-1までの乱数を生成できる
s = time()
result = C(27).h[:].m[:].run(1)
result = list(result)[0]
print(s-time())

print(int(result, 2))
