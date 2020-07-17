

def function():
    print("我的函数")


#object基类
class People(object):



    def hands(self,a,b):
        print("有两只手，可以吃饭")
        return a+b

    def foots(self):
        print("两只脚，可以走路！")


    def foots123(self):
        print("这是我的人，我想怎么就怎么！")
        # self.hands()      #self类本身的一个实例参数



#实例化----外部调用
xiaohua = People()
# xiaohua.hands(1,3)
print(xiaohua.hands(1,3))
xiaohua.foots()

xiaohua.foots123()




# print(xiaohua.hands())



