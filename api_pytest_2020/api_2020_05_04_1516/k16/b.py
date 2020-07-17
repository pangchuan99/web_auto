

def hello(a=10):
    while True:
        a = a+2
        print("a的值：%s"%a)
        # yield 相当于return
        yield a
        print("下次取值：*********")
        a = a+3
        print("yield的值：%s"%a)

b = hello(a=10)  # generator object
# print(b)
# print(next(b))
# print(next(b))
# print(next(b))
for i in range(10):
    print(next(b))