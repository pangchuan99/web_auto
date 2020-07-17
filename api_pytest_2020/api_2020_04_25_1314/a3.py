




#object基类
class People(object):
    #构造函数---初始化
    def __init__(self,age,name):

        #静态属性
        self.age=age
        self.name=name
        print("实例化的时候 自动执行__init__内容")



    def hands(self):
        print("有两只手，可以吃饭")


    def foots(self):
        print("我的名字是：{}".format(self.name))
        print("两只脚，可以走路！")


#一个类可以多次实例
xiaohua=People(age=20,name="xiaohua")
xiaohua123=People(age=21,name="xiaohua123")


age=xiaohua.age
print(age)
name=xiaohua.name
print(name)
xiaohua.hands()
xiaohua.foots()



#加其他属性
xiaohua.token="xxxxxxxxxxxxx"
print(xiaohua.token)




xiaohua123.foots()