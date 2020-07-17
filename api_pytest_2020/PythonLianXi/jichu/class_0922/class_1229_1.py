# from  selenium import  webdriver
# import  time
# we=webdriver.Chrome()
# we.get('https://ke.qq.com/')
# time.sleep(3)

class av:
    def __init__(self,a,b,n,k):
        self.a=a
        self.b=b
        self.n=n
        self.k=k


    def wadd(self,o,p):
        sum = 0
        for i in range(o, p):
             sum += i
        print("我要输出的值：",sum)

    def jian(self,a, b):
        print(a - b)

    # if __name__ == '__main__':
    #     wadd(1,101)

av(1,3,2,9).wadd(1,9)