



#父亲的
class Father():
    def __init__(self):
        self.name="laowangg"
        self.age=50


    def fangzi(self):
        print("父亲的房子")


    def chezi(self):
        print("父亲的车子")


#母亲的
class Mother():

    def gognsi(self):
        print("母亲开的公司")

#继承了 父类的（父亲和母亲的）
class Son(Father,Mother):
    def __init__(self):
        super().__init__()   #super  是初始化继承的时候，，，，要用到父类里面的属性  如果属性相同就参考儿子的  儿子也可以自己新增属性
        self.name="儿子"
        self.gexing="新增的个性"
    def cunkuan(self):
        print("儿子自己的存款")


     #覆盖掉了类型的方法
    def fangzi(self):
        super().fangzi()  #如果不想覆盖掉他只是在原有的基础上，加点东西，那么就用这个
        print("给房子加一些新的特性，，，自己的房子")
    def newfnagzi(self):
        self.fangzi()  #把名称换了

zilei=Son()
print(zilei.name)
print(zilei.age)
print(zilei.gexing)

zilei.chezi()
zilei.fangzi()
zilei.gognsi()
zilei.cunkuan()
