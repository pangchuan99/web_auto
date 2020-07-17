a = 1


class People(object):
    n = 2  #这个可以在 类里面进行调用  调用要使用self
    print("sss:%s"%n)

    def __init__(self, c=2):
        self.c = c  #所有方法都可以调用
        d = 4  # 局部的  只能在__init__里面调用
        self.g = "world"
        self.e = "hello"
        print(d)

    def hands(self, a, b):
        e = "hello"  #这个只能在 hands 方法里面调用
        print("有两只手，可以吃饭")
        print("n的值：%s"% self.n)
        return a+b

    def foots(self):
        print("c的值：%s"%self.c)
        print("两只脚，可以走路！")

    def get_g(self):
        print("g的值：%s"%self.g)

aa = People()
print(aa.n)
print(aa.hands("1", "a"))
# aa.get_g()