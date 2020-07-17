
# 快速生成列表 [1, 4, 8......81]
a = [i*i for i in range(1, 10)]
print(a)

# 生成器
b = (i*i for i in range(1, 10))
print(b)  # generator object
print(next(b))
print(next(b))
print(next(b))
 